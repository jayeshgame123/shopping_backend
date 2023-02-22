from django.db import models

# Create your models here.

class Product(models.Model):
    prod_img = models.ImageField(upload_to='media', blank=True, max_length=None)
    prod_name = models.TextField()
    prod_price = models.DecimalField(max_digits=12, decimal_places=2)
    prod_desc = models.TextField()
    
    def __str__(self):
        return self.prod_name


class User(models.Model):
    user_name = models.CharField(max_length=250)
    user_add = models.TextField()
    user_email = models.EmailField(max_length=254)
    user_mob = models.BigIntegerField(default=None)
    user_city = models.CharField(max_length=250)
    user_state = models.CharField(max_length=250)
    user_pincode = models.IntegerField(default=None)

class Cart(models.Model):
    userId = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class CartItems(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    prodId = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=None)

class Order(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(default=None)
    mobile = models.BigIntegerField(default=None)
    total = models.IntegerField(default=None)

class OrderItems(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    prodId = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default = None)
