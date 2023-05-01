from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('movies/', views.Movie.as_view(), name='movies'),
]