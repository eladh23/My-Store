from django.db import models
from django.contrib.auth.models import AbstractUser
from supermarket import settings


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    is_paid = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', related_name='cartitems', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"there is {self.quantity} of {self.product.name} in ({self.cart.user.username}'s Cart)"