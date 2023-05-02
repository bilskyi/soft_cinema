from typing import Any, Dict
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import *


class MovieDetail(DetailView):
    model = Movie
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'movie'
    template_name = 'home/movie_detail.html'

class Home(ListView):
    model = Movie
    template_name = 'home/home.html'
    context_object_name = 'movie'

class Movie(DetailView):
    model = Movie
    template_name = 'home/movies.html'
    context_object_name = 'movie'
    slug_url_kwarg = 'movie_slug'