from django.urls import path
from . import views

urlpatterns = [
    path('', views.theater, name='theater'),
    path('buy-ticket/<slug:movie_slug>/', views.buy_ticket, name='buy-ticket'),
    path('buy-ticket/<slug:movie_slug>/<slug:hall_slug>/', views.buy_ticket_hall, name='buy-ticket-hall'),
]