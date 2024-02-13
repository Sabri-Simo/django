from random import sample
from django.shortcuts import get_object_or_404, render
from .models import Product



# Create your views here.
def products(request,slug):
    product = get_object_or_404(Product, slug=slug)
    prod = list(Product.objects.all())  # Convert queryset to a list
    random_products = sample(prod, 4)  # Get 4 random products
    return render(request, 'Product/prot.html', {"product": product, "random_products": random_products})