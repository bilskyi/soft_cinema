from django.urls import path
from .views import confirm


urlpatterns = [
    path('confirm/<slug:movie_slug>', confirm, name='confirm')
]