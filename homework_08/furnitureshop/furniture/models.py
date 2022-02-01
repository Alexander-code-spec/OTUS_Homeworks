from django.db import models


class FurnitureSupplier(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)
    email = models.CharField(max_length=32, null=False)
    address = models.CharField(max_length=64, null=False)
    phone_number = models.IntegerField(null=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}    {self.email}'


class Furniture(models.Model):
    type = models.CharField(max_length=128)
    supplier = models.ForeignKey(FurnitureSupplier,
                                 on_delete=models.CASCADE,
                                 null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=False)

    class Meta:
        ordering = ['updated_at']

    def my_furniture(self):
        furniture = self.furniturematerial_set.all()
        return ', '.join(map(str, furniture))

    def __str__(self):
        return self.type


class FurnitureDetail(models.Model):
    furniture = models.OneToOneField('furniture.Furniture',
                                     primary_key=True,
                                     on_delete=models.CASCADE)
    discription = models.TextField()

    def __str__(self):
        return self.furniture


class FurnitureMaterial(models.Model):
    material = models.CharField(max_length=64, unique=True)
    furniture = models.ManyToManyField(Furniture)

    def __str__(self):
        return self.material


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Furniture)

    class Meta:
        default_related_name = 'stores'

    def __str__(self):
        return self.name