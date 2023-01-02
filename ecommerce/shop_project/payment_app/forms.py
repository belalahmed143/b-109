from django import forms 
from .models import ShipingAddress
from store.models import Order


class ShipingAddressForm(forms.Form):
    name = forms.CharField() 
    phone = forms.CharField()
    email  = forms.EmailField() 
    full_address = forms.CharField(widget=forms.Textarea()) 
    order_note = forms.CharField(widget=forms.Textarea()) 

Payment_Method =(
    ('Cash on delivery','Cash on delivery'),
    ('Bkash','Bkash'),
)

class PaymentMethodForm(forms.ModelForm):
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices =Payment_Method )
    class Meta:
        model = Order
        fields = ['payment_option']
