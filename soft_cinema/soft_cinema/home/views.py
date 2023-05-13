from typing import Any, Dict
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import *
from .utils import ContextMixin, MovieList

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

class Movie(MovieList, ContextMixin, ListView):
    template_name = 'home/movies.html'
    


class StateList(ContextMixin, ListView):
    model = State
    template_name = 'home/movies.html'
    context_object_name = 'movie'

    def get_queryset(self):
        state_slug = self.kwargs['state_slug']
        return self.model.objects.get(slug=state_slug).movie_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_slug = self.kwargs['state_slug']
        context['stage'] = self.model.objects.get(slug=state_slug)
        return context

