from django.shortcuts import render
from home.models import Movie

def confirm(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    return render(request, 'payment/confirm.html', {'movie': movie})
