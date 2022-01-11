from django.db import models
from user.models import User

class Furniture(models.Model):
    """
    Модель таблицы мебель
    """
    code = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True)
    name = models.CharField(max_length=32, unique=True)
    type = models.CharField(max_length=32, unique=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} <{self.email}>'
