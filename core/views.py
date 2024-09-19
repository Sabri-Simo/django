from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.db.models import Q

from product.models import Product,Category

from .forms import SignUpForm

def frontpage(request):
    products=Product.objects.all()[0:8]
    category=Category.objects.all()
    return render(request, 'Core/fontpage.html',{'products':products,'category':category})

def test(request):
    products=Product.objects.all()
    category=Category.objects.all()
    activeCategory=request.GET.get('category','')
    if activeCategory:
        products=products.filter(category__slug=activeCategory)
    
    query=request.GET.get('query','')
    if query:
        products=products.filter(name__icontains=query)

    return render(request, 'Core/test.html',{'products':products,'category':category,'activeCategory':activeCategory})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            User=form.save()
            
            login(request, User)
            # Process the form data if it's valid
            # For example, save the user to the database
            return redirect('login/')
            # Redirect to a success page or do something else
    else:
        # If it's a GET request, create a new instance of the form
        form = SignUpForm()      
    return render(request, 'core/singup.html',{'form':form})

def sinpage(request):
    return render(request,'core/singu.html')

def shopPage(request):
    products=Product.objects.all()
    category=Category.objects.all()
    activeCategory=request.GET.get('category','')
    if activeCategory:
        products=products.filter(category__slug=activeCategory)
    
    query=request.GET.get('query','')
    if query:
        products=products.filter(name__icontains=query)
    
    return render(request, 'Core/shop.html',{'products':products ,'category':category,'activeCategory':activeCategory})



