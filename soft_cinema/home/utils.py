'''utils'''

from .models import Movie


class MovieList:
    model = Movie
    template_name = 'home/home.html'
    context_object_name = 'movie'