from django.urls import path
from django.contrib import admin

import furniture.views as furnitures


app_name = 'furniture'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', furnitures.furniture_list,
         name='furniture_list'),
    path('<slug:category_slug>/',
         furnitures.furniture_list,
         name='furniture_list_category'),
    path('<int:id>/<slug:slug>',
         furnitures.furniture_detail,
         name='furniture_detail')
]

