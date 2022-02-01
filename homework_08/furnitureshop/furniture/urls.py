from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

import furniture.models
import furniture.views as furnitures


app_name = 'furniture'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', furnitures.index, name='index'),
    path('furniture/',
         furnitures.FurnitureListView.as_view(),
         name='list'),
    path('furniture/supplier_detail/<int:pk>/',
         furnitures.FurnitureSupplierDetailView.as_view(template_name="furniture/supplier_detail.html"),
         name='supplier'),
    path('furniture/update/<int:item_pk>/',
         furnitures.FurnitureUpdateView.as_view(template_name="furniture/furniture_update.html"),
         name='furniture_update'),
    path('furniture/material_detail/<int:pk>/',
         furnitures.FurnitureMaterialDetailView.as_view(template_name="furniture/material_detail.html"),
         name='furniture_material'),
    # path('animals/create/',
    #      animals.AnimalKindCreateView.as_view(),
    #      name='animalkind_create'),
    # path('animals/update/<int:item_pk>/',
    #      animals.AnimalKindUpdateView.as_view(),
    #      name='animalkind_update'),
    #
    # # path('about/', animals.about, name='about'),
    # path('about/',
    #      TemplateView.as_view(template_name='animals/about.html'),
    #      name='about'),
]

