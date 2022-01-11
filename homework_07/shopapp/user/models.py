from django.db import models



class User(models.Model):
    """
    Модель таблицы пользователя
    """

    name = models.CharField(max_length=32, unique=True)
    email = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} <{self.email}>'

    class Meta:
        verbose_name = 'Имя пользователя'
        ordering = ['name']