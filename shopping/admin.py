from django.contrib import admin
from .models import Product,Cart,User,Order,CartItems
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(CartItems)