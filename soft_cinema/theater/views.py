from typing import Any, Dict
from django.shortcuts import render
from home.models import Movie
from .models import Seat
from .forms import SeatForm
from django.views.generic import DetailView

def theater(request):
    return render(request, 'theater/theater.html')


def buy_ticket(request, movie_slug):
    movie = Movie.objects.filter(slug=movie_slug)
    return render(request, 'theater/buy_ticket.html', {'movie': movie})


def select_seat(request):
    seats = Seat.objects.filter(available=True)
    return render(request, 'theater/select.html', {'seats': seats})


class BuyTicket(DetailView):
    model = Movie
    template_name = 'theater/buy_ticket.html'
    context_object_name = 'movie'
    slug_url_kwarg = 'movie_slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = SeatForm
        return context