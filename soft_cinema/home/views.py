from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home/home.html')

#test view
def movies(request):
    movie = Movie.objects.all()
    return render(request, 'home/movies.html', {'movie': movie})