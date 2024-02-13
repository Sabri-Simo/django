from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from django.urls import path
from core.views import frontpage,shopPage,signup,loginn,stem
from product.views import products
from cart.views import add_to_cart,cart,checkOut

urlpatterns = [
    path('',frontpage,name='frontpage'),
    path('signupage/',signup,name='singupPgae'),
    path('stem/',stem,name='stem'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('log/',loginn,name='logg'),
    path('login/',views.LoginView.as_view(template_name='Core/login.html'),name='loginPage'),
    path('shop/',shopPage,name='shopPage'),
    path('shop/<slug:slug>/',products, name='product'),
    path('shop/<slug:slug>/',products, name='prod'),
    path('cart',cart,name='cart'),
    path('cart/checkout/',checkOut,name='check'),
    path('add_to_cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)