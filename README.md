# ECE568 Final Project - Mini-Amazon

### Introduction

This is a scalable full-stack web application simulating Amazon where the users can browse products, buy them, and track the order. The application is implemented using Django and PostgreSQL. 

### App Deployment



![image](https://github.com/jyf9870/Mini-Amazon/assets/80262336/cab91d32-5415-4732-88ce-d49167de8017)

Three essential parts are needed for the complete functionality of this app.

1. Mini Amazon (this application itself)
2. Mini UPS (implemented by other teams)
3. World (a warehouse system under the world_simulator_exec directory)



### App Features

**Login/Sign up**

![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2FfcZQHbcvrjTaKCcP4nBs%2Fimage.png?alt=media&token=78e76cf0-39d1-4d71-98c5-6bbf0b469c6b)

![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2FP2AUurr5Q1r2DiVvviSV%2Fimage.png?alt=media&token=8b36d813-8efa-4332-8dd9-d255aca90b02)



The user is able to login to the Mini Amazon store or sign up for a new account. Django authentication is used to ensure security and robustness of the web application.

**Search and Filter**



![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2FjGViDn3QE82b8J8xZfZg%2Fimage.png?alt=media&token=2ed8ae75-e1f8-43c2-a6a5-f7b4c29ee69c)

![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2FJtQ9pu8O63mtqIkkYghm%2Fimage.png?alt=media&token=fbe1a1a9-5c97-4a73-88a9-e43d688a1891)



![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2FCVFdU7ayocZqNAhrrw5G%2Fimage.png?alt=media&token=5a56a7cf-a07c-4d7c-b82b-24d290bcd3a9)



![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2Frbh0nZjjZGAL3KHuP8Or%2Fimage.png?alt=media&token=fea57590-468d-4376-8eb3-4f85fb93c36e)

![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2FuwoDg0gB4HpuWJLhkUHM%2Fimage.png?alt=media&token=76c082b7-cf6f-4877-af57-8cddd867bd58)

Users have the convenience of searching for various product categories available in the web store, such as gloves, enhancing their browsing experience. Additionally, a user-friendly categories dropdown feature allows for effortless filtering of desired items, ensuring a seamless shopping experience.

**Place Orders**

![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2Fdg4R9prdSWk5sQkFzEwN%2Fimage.png?alt=media&token=25e41f17-5e16-44a4-93b8-941564bf545f)

The user can buy products by placing an order where they specify their address (a Cartesian coordinate), product, product count, and their email. Once the order is placed, a confirmation email will be sent to the user.

**Check Order Status**
The user can check the status of any of their orders. The time that takes to process the orders depends on the speed of the world simulator, whose details can be read in this repo:

https://github.com/yunjingliu96/world_simulator_exec



The status are updated according to the interactions among the three components of the app: Mini Amazon, Mini UPS, and the world simulator.

**Contact**

![img](https://1274107733-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MXD5c60uDzrjAPeW5GX%2Fuploads%2Fy3nKQfK7HBMb3K2GZenl%2Fimage.png?alt=media&token=7206f999-9293-4b68-9eb1-8a41780ae32a)

To facilitate effective communication between users and the Mini Amazon store, a user-friendly email functionality is incorporated, allowing users to easily send emails for inquiries or concerns. This feature ensures seamless interactions and fosters better customer support, enhancing overall user satisfaction.

## Authors: Yifan Jiang (yj193), Oliver Chen (yc557) 

## Notes to create local postgres database

```bash
sudo service postgresql start
sudo su - postgres
psql
CREATE user yc557;
ALTER USER yc557 WITH PASSWORD 'Oliver666';
CREATE DATABASE "projectDB";
GRANT ALL PRIVILEGES ON DATABASE "projectDB" TO yc557;
```

Quit postgresql, then connect to the db as the corresponding user

```bash
psql -d projectDB -U yc557
\dt
```

To stop postgres,

```bash
sudo service postgresql stop
```

## Notes related to Docker

To create a superuser in Django within Docker, first use `docker ps` to
get the container id, then

```bash
sudo docker exec -it <container_id> python3 manage.py createsuperuser
```

To enter into a Docker container:

```bash
docker exec -it <container_id_or_name> bash
```
