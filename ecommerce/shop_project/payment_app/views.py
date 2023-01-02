from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from store.models import *
from django.contrib import messages
# Create your views here.

class Checkout(View):
    def get(self, request, *args, **kwargs):
        form = ShipingAddressForm()
        payment_method = PaymentMethodForm()
        order = Order.objects.filter(user=request.user, ordered=False)
        context ={
            'form':form,
            'payment_method':payment_method,
            'order':order
        }
        return render(request, 'payment_app/checkout.html',context)
         
    def post(self, request, *args, **kwargs):
        form = ShipingAddressForm(request.POST)
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        pay_form = PaymentMethodForm(instance=payment_obj)

        if request.method == 'POST':
            form = ShipingAddressForm(request.POST)
            pay_form = PaymentMethodForm(request.POST,instance=payment_obj)

            if form.is_valid() and pay_form.is_valid():
                name = form.cleaned_data.get('name')
                phone =form.cleaned_data.get('phone')
                email =form.cleaned_data.get('email')
                full_address =form.cleaned_data.get('full_address')
                order_note =form.cleaned_data.get('order_note')

                shiping_address = ShipingAddress(
                    user = request.user,
                    name = name,
                    phone = phone,
                    email = email,
                    full_address = full_address,
                    order_note = order_note,
                )
                shiping_address.save()
                payment_obj.shiping_address=shiping_address
                pay_method = pay_form.save()

                if pay_method.payment_option == 'Cash on delivery':
                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order = order_qs[0]
                    order.ordered = True
                    order.payment_option = pay_method.payment_option
                
                    cart_products = CartProduct.objects.filter(user=request.user, ordered=False)
                    
                    for cart_product in cart_products:
                        cart_product.ordered = True
                        cart_product.save()
                    order.save()
                    messages.success(request, 'You order was successfully done')
                    return redirect('/')
                else:
                    return redirect('checkout')
            else:
                return redirect('checkout')
        else:
            return redirect('checkout')
        