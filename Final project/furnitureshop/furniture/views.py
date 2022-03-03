from django.core.paginator import Paginator
from cart.forms import CartAddProductForm
from furniture.models import Furniture, Category
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'furniture/index.html')


def furniture_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    furnitures = Furniture.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        furnitures = furnitures.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'furnitures': furnitures,
    }
    return render(request,
                  'furniture/furniture_list.html',
                  context=context)


def furniture_detail(request, id, slug):
    funriture = get_object_or_404(Furniture,
                                  id=id,
                                  slug=slug,
                                  available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'furniture': funriture,
        'cart_product_form': cart_product_form
    }
    return render(request,
                  'furniture/furniture_detail.html',
                  context=context)

