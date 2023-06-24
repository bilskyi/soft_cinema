from typing import Any, Dict
from django.shortcuts import redirect, render, get_object_or_404
from home.models import Movie
from .models import Seat, Hall
from .forms import SeatForm
from django.views.generic import DetailView


def theater(request):
    return render(request, 'theater/theater.html')


def buy_ticket(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    seats = Seat.objects.all()

    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            selected_seats = form.cleaned_data['seat']
            for seat in selected_seats:
                # Assuming 'number' uniquely identifies a seat
                seat_movie = Seat.objects.get(number=seat.number)
                seat_movie.user = request.user
                seat_movie.is_available = False
                seat_movie.save()
            return redirect('movies')

    else:
        form = SeatForm()

    context = {
        'movie': movie,
        'form': form,
        'seats': seats,
    }
    
    return render(request, 'theater/buy_ticket.html', context=context)