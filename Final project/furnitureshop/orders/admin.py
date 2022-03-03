from django.contrib import admin
from orders.models import Order, OrderInstance


class OrderItemInline(admin.TabularInline):
    model = OrderInstance
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'email',
                    'address', 'paid',
                    'created_at', 'updated_at']
    list_filter = ['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
