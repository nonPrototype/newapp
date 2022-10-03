from django.contrib import admin

from .models.client import Client
from .models.purchase import Purchase
from .models.product import Product

# Register your models here.

admin.site.register(Client)
admin.site.register(Purchase)
admin.site.register(Product)
