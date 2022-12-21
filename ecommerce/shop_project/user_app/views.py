from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_app/registration.html',{'form':form})

def profile(request):
    return render(request, 'user_app/profile.html')

def profile_update(request):
    if request.method == 'POST':
        user_form = UserRegistrationUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Successfully updated')
            return redirect('profile')
    else:
        user_form = UserRegistrationUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.profile)

    return render(request, 'user_app/profile-update.html', {'user_form':user_form, 'profile_form':profile_form})
    

    
