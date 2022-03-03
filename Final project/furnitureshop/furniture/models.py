from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=120, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def _str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('furniture:furniture_list_category', args=[self.slug])


class Furniture(models.Model):
    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.CASCADE,)
    name = models.CharField(max_length=64, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('furniture:furniture_detail', args=[self.id, self.slug])
