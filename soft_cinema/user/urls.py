from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
]