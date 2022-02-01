from django.contrib import admin

from furniture.models import Furniture, FurnitureSupplier, FurnitureMaterial

admin.site.register(Furniture)
admin.site.register(FurnitureSupplier)
admin.site.register(FurnitureMaterial)

# Register your models here.
