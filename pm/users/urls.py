from django.urls import path
from django.contrib.auth.decorators import login_required

from users import views

urlpatterns = [
    path('myhome/', views.MyHomeView.as_view(), name='myHome'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/p/<int:pk>/', views.UpdateProfileView.as_view(),
         name='profileUpdate'),
    path('profile/u/<int:pk>/', views.UpdateUserDataView.as_view(),
         name='userdataUpdate'),
]
