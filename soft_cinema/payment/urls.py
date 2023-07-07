from django.urls import path
from .views import confirm


urlpatterns = [
    path('confirm/<slug:movie_slug>/<slug:hall_slug>/', confirm, name='confirm')
]