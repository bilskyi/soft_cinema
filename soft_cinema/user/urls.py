from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<slug:username_slug>/', views.profile, name='profile')
]