from typing import Any, Dict
from django.shortcuts import redirect, render
from home.models import Movie
from .models import Seat
from .forms import SeatForm
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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = SeatForm
        context['row'] = Seat.objects.values('row').distinct()
        context['seat'] = Seat.objects.values('seat').distinct()
        return context


def buy_ticket(request, movie_slug):
    movie = Movie.objects.filter(slug=movie_slug)
    form = SeatForm
    row = Seat.objects.values('row').distinct()
    seat = Seat.objects.values('seat').distinct()
    context = {
        'movie': movie,
        'form': form,
        'row': row,
        'seat': seat,
    }
    if request.method == 'POST':
        form = SeatForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('movies')
    return render(request, 'theater/buy_ticket.html', context=context)
