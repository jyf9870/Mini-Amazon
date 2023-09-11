# from .ups import UPS
from .world import World
from .ups import UPS

import socket

HOST_WORLD = 'vcm-32169.vm.duke.edu'
PORT_WORLD = 23456

SIMSPEED = 10000


class Backend():
    def __init__(self):
        self.ups = UPS()
        print("Binding")
        try:
            self.ups.server_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self.ups.server_socket.bind(("vcm-32290.vm.duke.edu", 54321))
        except OSError:
            print("Socket already bound")
            return
        else:
            print("Socket bound successfully")
        self.ups.connect(SIMSPEED)
        print('Ups initialized')
        self.world = World(HOST_WORLD, PORT_WORLD, SIMSPEED)
        print('Initialized world.')
        self.ups.setWorld(self.world)
        self.world.setUPS(self.ups)
        print('Set completed')
        self.ups.init()
        print('Initialized backend.')
    
    def buy(self, pid, whid, count):
        self.world.purchase_more(pid, whid, count)

    def pack(self, pkgid):
        self.world.pack(pkgid)

    def refresh(self):
        self.world.query()
        
    def get_world(self):
        return self.world
