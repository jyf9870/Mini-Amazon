from django.contrib import admin
from .models import Order, Stock, Warehouse, Product
# Register your models here.
admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(Warehouse)
admin.site.register(Product)
