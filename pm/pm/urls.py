"""pm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from users import forms, views
from django.contrib.auth import get_user_model

User = get_user_model()


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]
