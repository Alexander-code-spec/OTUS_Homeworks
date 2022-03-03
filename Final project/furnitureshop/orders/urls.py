from django.urls import path
from django.contrib import admin

import orders.views as order


app_name = 'order'

urlpatterns = [
    path('create/', order.order_create,
         name='order_create'),
]
