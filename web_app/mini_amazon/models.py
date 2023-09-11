from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.IntegerField(
        default=-1, verbose_name='Destination X Value')
    y = models.IntegerField(
        default=-1, verbose_name='Destination Y Value')
    pkgid = models.IntegerField(default=-1)
    pid = models.IntegerField(
        default=-1, verbose_name='Product ID')
    count = models.IntegerField(
        default=-1, verbose_name='Product Count')
    whid = models.IntegerField(default=0)
    truckid = models.IntegerField(default=-1)
    status = models.CharField(max_length=100, default="", blank=True)
    email = models.EmailField(max_length=254, default='default@gmail.com')


class Stock(models.Model):
    pid = models.IntegerField(default=-1)
    count = models.IntegerField(default=-1)
    worldid = models.IntegerField(default=-1)
    whid = models.IntegerField(default=-1)


class Warehouse(models.Model):
    whid = models.IntegerField(default=-1)
    x = models.IntegerField(default=-1)
    y = models.IntegerField(default=-1)


class Product(models.Model):
    pid = models.IntegerField(default=-1)
    description = models.CharField(max_length=1000, default="")
    catalog = models.IntegerField(default=-1)
    pic = models.CharField(max_length=1000, default="")
    price = models.IntegerField(default=-1)
