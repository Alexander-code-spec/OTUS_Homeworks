from django.contrib import admin

from furniture.models import Furniture, Category


@admin.register(Category)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

