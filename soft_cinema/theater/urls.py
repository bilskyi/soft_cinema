from django.urls import path
from . import views

urlpatterns = [
    path('', views.theater, name='theater'),
    path('select/', views.select_seat, name='select'),
    path('buy-ticket/<slug:movie_slug>/', views.BuyTicket.as_view(), name='buy-ticket'),
]