from django.contrib import admin
from vendor.models import Vendor, Order, FoodItem, OrderDetail

admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(FoodItem)
admin.site.register(OrderDetail)
# Register your models here.
