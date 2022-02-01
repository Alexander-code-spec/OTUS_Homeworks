from datetime import time

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView
from furniture.models import Furniture, FurnitureSupplier, FurnitureMaterial

from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


class FurnitureListView(ListView):
    model = Furniture
    ordering = ['-updated_at']


class FurnitureSupplierDetailView(DetailView):
    model = FurnitureSupplier


class FurnitureMaterialDetailView(DetailView):
    model = FurnitureMaterial


class FurnitureUpdateView(UpdateView):
    model = Furniture
    success_url = reverse_lazy('furniture:list')
    fields = ('type',)
    pk_url_kwarg = 'item_pk'