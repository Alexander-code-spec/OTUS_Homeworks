from django.contrib.auth.models import AbstractUser
from django.db import models
from orders.models import Order


class ShopUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)



