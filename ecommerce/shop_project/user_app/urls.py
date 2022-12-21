from django.urls import path 
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', registration, name='registration'),
    path('login', auth_views.LoginView.as_view(template_name = 'user_app/login.html') , name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'user_app/logout.html') , name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user_app/password-change.html'), name='password-change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user_app/password-change_done.html'), name='password_change_done'),
    
    path('profile', profile, name='profile'),
    path('profile/update', profile_update, name='profile-update'),
]