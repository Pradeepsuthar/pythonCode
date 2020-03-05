from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopPage"),
    path('about/', views.aboutUs, name="AboutUs"),
    path('contact/', views.contactUs, name="ContactUs"),
    path('track/', views.tracking, name="TrackingStatus"),
    path('search/', views.searching, name="Search"),
    path('checkout/', views.checkoutPage, name="Checkout"),
    path('products/<int:id>', views.viewProduct, name="products"),
    path('mensware/', views.forMenCategory, name="men"),
    path('womensware/', views.forWoMenCategory, name="women"),
    path('kidsware/', views.forKidsCategory, name="kids"),
    path('signup/', views.register, name="signup"),
    path('cart/', views.cart, name="shopingCart"),
    
]