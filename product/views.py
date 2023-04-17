from django.shortcuts import render


# Create your views here.

def cart(request):
    return render(request, 'product/cart.html')

def checkout(request):
    return render(request, 'product/checkout.html')

def home(request):
    return render(request, 'product/home.html')

def login(request):
    return render(request, 'product/login.html')

def shop(request):
    return render(request, 'product/shop.html')

def singleproduct(request):
    return render(request, 'product/singleproduct.html')

def register(request):
    return render(request, 'product/register.html')
