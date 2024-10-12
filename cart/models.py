from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
