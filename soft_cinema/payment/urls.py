from django.urls import path
from .views import confirmation


urlpatterns = [
    path('confirmation/<slug:movie_slug>/<slug:hall_slug>/', confirmation, name='confirm')
]