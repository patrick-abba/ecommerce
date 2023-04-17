from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('shop/', views.shop, name = 'shop'),
    path('cart/', views.cart, name = 'cart'),
    path('singleproduct/', views.singleproduct, name = 'singleproduct'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register')
       
]