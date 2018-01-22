from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, password_change, logout

from users import forms, views


urlpatterns = [
    path('myhome/', views.MyHomeView.as_view(), name='myHome'),
    #    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', login,
         {'authentication_form': forms.LoginForm}, name='login'),
    path('change_password/', password_change,
         {'password_change_form': forms.PasswordForm,
          'template_name': 'users/password_change.html',
          'post_change_redirect': '/users/profile/',
          'extra_context': {'message': 'Password successfully updated'}},
         name='password_change'), path('admin/', admin.site.urls),
    path('logout', logout, {'next_page': 'home'}, name='auth_logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/p/<int:pk>/', views.UpdateProfileView.as_view(),
         name='profileUpdate'),
    path('profile/u/<int:pk>/', views.UpdateUserDataView.as_view(),
         name='userdataUpdate'),
]
