from .utils import Utils
from . import world_amazon_pb2
from . import amazon_ups_pb2
from mini_amazon.models import Order, Stock, Product, Warehouse
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.encoder import _EncodeVarint

import threading
import socket
import time


class UPS():

    def init(self):
        msg = amazon_ups_pb2.UAstart()
        raw_byte = self.recv()
        msg.ParseFromString(raw_byte)
        print("Received world: ", msg)
        msg_init = amazon_ups_pb2.AUCommand()
        msg_init.acks.append(msg.seqnum)
        self.send(msg_init)
        self.world.init(msg.worldid)
        # update stock
        stocks = Stock.objects.all()
        for s in stocks:
            s.worldid = msg.worldid
            s.save()
        # start processing response
        print("Starting processing...")
        responseHandler = threading.Thread(
            target=self.process_response, args=())
        responseHandler.setDaemon(True)
        responseHandler.start()

    def setWorld(self, world):
        self.world = world

    """
    // UPS to Amazon: UPS creates a world for Amazon to connect to
    message UAstart {
        required int64 worldid = 1;
        required int64 seqnum = 2;
    }
    """

    # def set_world(self):
    #     msg = amazon_ups_pb2.UAstart()
    #     raw_byte = self.recv()
    #     msg.ParseFromString(raw_byte)
    #     print("Received world: ", msg)
    #     msg_init = amazon_ups_pb2.AUCommand()
    #     msg_init.acks.append(msg.seqnum)
    #     self.send(msg_init)
    #     self.world.init(msg.worldid)
    #     return msg

    """
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    """

    def receive(self):
        print("Receiving...")
        msg = amazon_ups_pb2.UACommand()
        raw_byte = self.recv()
        msg.ParseFromString(raw_byte)
        print("Received message: ", msg)
        return msg

    """
    // request
    message AUCommand{
        repeated AUPickupRequest pickupRequests = 1;
        repeated AUDeliverRequest deliverRequests = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // Amazon to UPS: when Amazon received a Buy command, it send APickupRequest to UPS to prepare a truck sent to target warehouse
    message AUPickupRequest{
        required int64 seqNum = 1;
        required int64 shipId = 2;
        required int32 warehouseId = 3;
        required int32 x = 4; // location of the warehouse
        required int32 y = 5; // location of the warehouse
        required int32 destinationX = 6;
        required int32 destinationY = 7;
        optional string upsName = 8;
        required string items = 9;
    }
    """

    def pickup_request(self, worldOrder):
        print("Processing pickup request")
        msg = amazon_ups_pb2.AUCommand()
        truck = msg.pickupRequests.add()
        # warehouse info
        truck.warehouseId = worldOrder.whid
        wh = Warehouse.objects.get(whid=worldOrder.whid)
        truck.x = wh.x
        truck.y = wh.y
        # destination info
        truck.destinationX = worldOrder.x  # NOTE: check
        truck.destinationY = worldOrder.y
        truck.shipId = worldOrder.pkgid
        # add item info
        # TODO: delete this
        # product = Product.objects.get(pid=worldOrder.pid)
        # truck.items.append(product.description)
        truck.items = "TEST"
        # update sequence number
        self.seq_num += 1
        temp = self.seq_num
        truck.seqNum = temp
        self.seq_dict[temp] = msg
        # send message
        self.send(msg)

    """
    // request
    message AUCommand{
        repeated AUPickupRequest pickupRequests = 1;
        repeated AUDeliverRequest deliverRequests = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // A -> U: when all ready, make UPS deliver the package
    message AUDeliverRequest{
        required int64 seqNum = 1;
        required int64 shipId = 2;
    }
    """

    def deliver_request(self, worldOrder):
        print("Processing deliver request")
        msg = amazon_ups_pb2.AUCommand()
        loaded = msg.deliverRequests.add()
        loaded.shipId = worldOrder.pkgid
        # update sequence number
        self.seq_num += 1
        temp = self.seq_num
        loaded.seqNum = temp
        self.seq_dict[temp] = msg
        # send message
        self.send(msg)

    """
    // response
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // U -> A Arrived, ready to load
    message UALoadRequest{
        required int64 seqNum = 1;
        required int32 truckId = 2;
        required int64 shipId = 3;
    }
    """

    def load_request(self, arrived):
        print("Processing load request")
        UPSOrder = Order.objects.get(pkgid=arrived.shipId)
        UPSOrder.truckid = arrived.truckId
        UPSOrder.save()
        UPSOrder = Order.objects.get(truckid=arrived.truckId)
        self.world.put_on_truck(UPSOrder)
        return arrived.seqNum

    """
    // response
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // U -> A: delivered
    message UADelivered{
        required int64 seqNum = 1;
        required int64 shipId = 2;
    }
    """

    def package_delivered(self, delivered):
        print("Processing delivered")
        return delivered.seqNum

    """
    // response
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    """

    def process_response(self):
        print("Processing response")
        while True:
            msg = self.receive()
            back = amazon_ups_pb2.AUCommand()
            # truck has arrived, ready to load
            for lr in msg.loadRequests:
                if lr.seqNum not in self.recv_msg:
                    self.recv_msg.add(lr.seqNum)
                    back.acks.append(self.load_request(lr))
            # package delivered
            for d in msg.delivered:
                if d.seqNum not in self.recv_msg:
                    self.recv_msg.add(d.seqNum)
                    back.acks.append(self.package_delivered(d))
            for ack in msg.acks:
                self.seq_dict.pop(ack, None)
            # send back
            self.send(back)

    def connect(self, simspeed=100):
        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_socket.listen()
        self.simspeed = simspeed
        self.seq_num = 0
        self.seq_dict = dict()
        self.recv_msg = set()
        print("Here1")

        client_socket, client_address = self.server_socket.accept()
        print("Here2")
        self.socket = client_socket
        print("Here3")

        th_resend = threading.Thread(target=self.resend, args=())
        th_resend.setDaemon(True)
        th_resend.start()

    def __del__(self):
        self.socket.close()

    def send(self, msg):
        print("Sending message: \n" + str(msg))
        if str(msg) != "":
            data_string = msg.SerializeToString()
            _EncodeVarint(self.socket.send, len(data_string), None)
            self.socket.send(data_string)

    def recv(self):
        var_int_buff = []
        while True:
            buf = self.socket.recv(1)
            var_int_buff += buf
            msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
            if new_pos != 0:
                break
        whole_message = self.socket.recv(msg_len)
        return whole_message

    def resend(self):
        while True:
            time.sleep(1)
            for k in self.seq_dict:
                self.send(self.seq_dict[k])
