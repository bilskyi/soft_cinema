from django.views.generic import ListView
from django.shortcuts import render
from .models import *


class Home(ListView):
    model = Movie
    template_name = 'home/home.html'
    context_object_name = 'movie'

class Movie(ListView):
    model = Movie
    template_name = 'home/movies.html'
    context_object_name = 'movie'