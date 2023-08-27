'''utils'''
from .models import Movie, State


class MovieList:
    model = Movie
    template_name = 'home/home.html'
    context_object_name = 'movie'
    

class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        states = State.objects.all()
        context['states'] = states
        return context