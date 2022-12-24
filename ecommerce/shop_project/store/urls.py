from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/detail/<pk>', product_detail, name='product-detail'),
    path('product-search/', product_search, name='product-search'),
    path('category-filter/<pk>', category_filtering, name='category-filter'),
    path('price-filter/<pk>', price_range_filter, name='price-filter'),
    path('add-to-cart/<pk>', add_to_cart, name='add-to-cart'),
]