from django.shortcuts import render
from home.models import Movie
from django.views.generic import DetailView

def theater(request):
    return render(request, 'theater/theater.html')


def buy_ticket(request, movie_slug):
    movie = Movie.objects.filter(slug=movie_slug)
    return render(request, 'theater/buy_ticket.html', {'movie': movie})


class BuyTicket(DetailView):
    model = Movie
    template_name = 'theater/buy_ticket.html'
    context_object_name = 'movie'
    slug_url_kwarg = 'movie_slug'
