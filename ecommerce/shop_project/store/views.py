from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
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


def add_to_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    cart_product, created = CartProduct.objects.get_or_create(product=product,user= request.user, ordered=False)
    order_qs = Order.objects.filter(user= request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            cart_product.quantity += 1
            cart_product.save()
            messages.info(request, 'Quantity updated')
            return redirect('product-detail',pk=product.pk)
        else:
            order.products.add(cart_product)
            messages.info(request, 'This Product Add to cart')
            return redirect('product-detail',pk=product.pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered=False,ordered_date=ordered_date)
        order.products.add(cart_product)
        messages.info(request, 'This Product Add to cart')
        return redirect('product-detail',pk=product.pk)


def cart_quantity_increment(request,pk):
    product = get_object_or_404(Product,pk=pk)
    cart_product, created = CartProduct.objects.get_or_create(product=product,user= request.user, ordered=False)
    order_qs = Order.objects.filter(user= request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            cart_product.quantity += 1
            cart_product.save()
            messages.info(request, 'Quantity updated')
            return redirect('cart-summary')
        else:
            return redirect('cart-summary')
    else:
        return redirect('cart-summary')


def cart_quantity_decrement(request,pk):
    product = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user= request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            cart_product = CartProduct.objects.filter(product=product,user= request.user, ordered=False)[0]
            if cart_product.quantity > 1:
                cart_product.quantity -= 1
                cart_product.save()
                messages.info(request, 'Quantity updated')
                return redirect('cart-summary')
            else:
                cart_product.delete()
                messages.info(request, 'Delete from cart')
                return redirect('cart-summary')
        else:
            return redirect('cart-summary')
    else:
        return redirect('cart-summary')


def remove_from_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user= request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            cart_product = CartProduct.objects.filter(product=product,user= request.user, ordered=False)[0]
            cart_product.delete()
            messages.info(request, 'Delete from cart')
            return redirect('cart-summary')
        else:
            return redirect('cart-summary')
    else:
        return redirect('cart-summary')

def cart_summary(request):
    order = Order.objects.get(user=request.user, ordered=False)
    context ={
        'order':order
    }
    return render(request,'store/cart-summary.html', context)