from django.urls import path
from . import views

urlpatterns = [
    path('product', views.products, name="products"), 
    path('product/<id>', views.product_detail, name="product_detail"),  
    path('carts', views.carts, name="carts"),
    path('carts/<id>', views.cart_detail, name="cart_detail"),
    path('cartsItem', views.cartsItem, name="cartsItem"),
    path('cartsItem/<id>', views.cartItem_detail, name="cartItem_detail"),
]
