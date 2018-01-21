"""pm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import login, password_change, logout
from users import forms, views
from users.views import UserRegistrationView
from django.contrib.auth import get_user_model

User = get_user_model()


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('accounts/register/', UserRegistrationView.as_view(), name='register'),
    path('accounts/login/', login,
         {'authentication_form': forms.LoginForm}, name='login'),
    path('accounts/change_password/', password_change,
         {'password_change_form': forms.PasswordForm,
          'template_name': 'users/password_change.html',
          'post_change_redirect': '/users/profile/',
          'extra_context': {'message': 'Password successfully updated'}},
         name='password_change'), path('admin/', admin.site.urls),
    path('accounts/logout', logout, name='auth_logout'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]
