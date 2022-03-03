from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from furniture.models import Furniture
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Furniture,
                                id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update=cd['update'])
    return redirect('cart:detail')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Furniture, id=id)
    cart.remove(product)
    return redirect('cart:detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    context = {
        'cart': cart
    }

    return render(request, 'cart/detail.html', context)
