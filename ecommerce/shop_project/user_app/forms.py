from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class UserRegistrationUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'first_name', 'last_name']

class UserProfileUpdateForm(forms.ModelForm):
    dobd = forms.CharField(required=False,widget=forms.DateInput(attrs={
        'type':'date'
    }))
    phone = forms.CharField(required=False, widget=forms.NumberInput())
    class Meta:
        model = Profile 
        fields = '__all__'
        exclude = ('user',)
        