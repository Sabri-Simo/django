from django.shortcuts import render
from .cart import Cart
# Create your views here.

def add_to_cart(request,product_id):
    cart=Cart(request)
    cart.add(product_id)
    
    return render(request, 'cart/menu_cart.html')


def cart (request):
    return render(request, 'cart/cart.html')

def checkOut(request):
    return render(request,'cart/checkout.html')