from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
# Create your views here.

def home(request):
    banners =Banner.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    
    context ={
        'banners':banners,
        'categories':categories,
        'products':products,
    }
    return render(request, 'store/index.html',context)

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    related_product = Product.objects.filter(category=product.category).exclude(pk=pk)
    context ={
        'product':product,
        'related_product':related_product
    }
    return render(request, 'store/product-detail.html',context)


def product_search(request):
    query = request.GET['q']
    lookup = Q(name__icontains=query) | Q(price__icontains=query) | Q(discount_price__icontains=query) | Q(category__name__icontains=query) | Q(barnd__name__icontains=query)
    products = Product.objects.filter(lookup)
    context ={
        'products':products
    }
    return render(request, 'store/product-search.html',context)

from django.core.paginator import Paginator

def category_filtering(request,pk):
    price_range = PriceRange.objects.all()
    cate = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=cate.id)


    paginator = Paginator(products, 1) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context ={
        'page_obj':page_obj,
        'price_range':price_range
    }
    return render(request, 'store/category-filter.html',context)

def price_range_filter(request,pk):
    price = get_object_or_404(PriceRange, pk=pk)
    products = Product.objects.filter(price_range=price.id)
    price_range = PriceRange.objects.all()
    context ={
        'products':products,
        'price_range':price_range
    }
    return render(request, 'store/price-filter.html',context)