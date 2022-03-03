from django.urls import path
import cart.views as view


app_name = 'cart'

urlpatterns = [
    path('cart_detail/', view.cart_detail, name='detail'),
    path('add/<int:id>/', view.cart_add, name='cart_add'),
    path('remove/<int:id>/', view.cart_remove, name='cart_remove'),
]