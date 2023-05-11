from typing import Any, Dict
from django.shortcuts import redirect, render
from home.models import Movie
from .models import Seat
from .forms import SeatForm
from django.views.generic import DetailView

def theater(request):
    return render(request, 'theater/theater.html')


def buy_ticket(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    seats = Seat.objects.filter(is_available=True)
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            selected_seats = form.cleaned_data['seat']
            for seat in selected_seats:
                seat.is_available = False
                seat.movie = movie
                seat.save()
            return redirect('movies')
    else:
        form = SeatForm()
    context = {
        'movie': movie,
        'form': form,
        'seats': seats,
    }
    return render(request, 'theater/buy_ticket.html', context=context)
