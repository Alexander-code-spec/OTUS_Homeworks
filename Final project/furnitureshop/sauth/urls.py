from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import sauth.views as auth

app_name = 'user'

urlpatterns = [
    path('user/create/',
         auth.ShopUserCreateView.as_view(),
         name='user_create'),
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
]