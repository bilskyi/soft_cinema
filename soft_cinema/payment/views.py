from django.shortcuts import render
from home.models import Movie
from theater.models import Hall

def confirmation(request, movie_slug, hall_slug):
    movie = Movie.objects.get(slug=movie_slug)
    hall = Hall.objects.get(slug=hall_slug)
    return render(request, 'payment/confirm.html', {'movie': movie, 'hall': hall})