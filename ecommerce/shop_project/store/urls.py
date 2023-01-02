from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/detail/<pk>', product_detail, name='product-detail'),
    path('product-search/', product_search, name='product-search'),
    path('category-filter/<pk>', category_filtering, name='category-filter'),
    path('price-filter/<pk>', price_range_filter, name='price-filter'),
    path('add-to-cart/<pk>', add_to_cart, name='add-to-cart'),
    path('cart-summary/', cart_summary, name='cart-summary'),
    path('cart_quantity_increment/<pk>/',cart_quantity_increment,name='cart_quantity_increment'),
    path('cart_quantity_decrement/<pk>/',cart_quantity_decrement,name='cart_quantity_decrement'),
    path('remove_from_cart/<pk>/',remove_from_cart,name='remove_from_cart'),
]