from django.urls import path
from . import views

urlpatterns = [
    path('', views.theater, name='theater'),
    path('buy-ticket/<slug:movie_slug>/', views.buy_ticket, name='buy-ticket'),
]