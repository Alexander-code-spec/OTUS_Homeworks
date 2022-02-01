from django.contrib import admin

from furniture.models import Furniture, FurnitureSupplier, FurnitureMaterial, Store, FurnitureDetail

admin.site.register(Furniture)
admin.site.register(FurnitureSupplier)
admin.site.register(FurnitureMaterial)
admin.site.register(Store)
admin.site.register(FurnitureDetail)


# Register your models here.
