from django.shortcuts import render
from .models import *


def home(request):
    movie = Movie.objects.all()
    return render(request, 'home/home.html', {'movie': movie})

#test view
def movies(request):
    movie = Movie.objects.all()
    return render(request, 'home/movies.html', {'movie': movie})