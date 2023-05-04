from typing import Any, Dict
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import *
from .utils import MovieList

class MovieDetail(DetailView):
    model = Movie
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'movie'
    template_name = 'home/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = self.object.cat.all()
        context['categories'] = categories
        return context

class Home(MovieList, ListView):
    pass

class Movie(MovieList, ListView):
    template_name = 'home/movies.html'
    queryset = {'states'}


class StateList(DetailView):
    model = Movie
    template_name = 'home/movies.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        states = self.object.state.all()
        context['states'] = states
        return context
