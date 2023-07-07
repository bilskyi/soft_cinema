from typing import Any, Dict
from django.shortcuts import redirect, render, get_object_or_404
from home.models import Movie
from .models import Seat, Hall
from .forms import SeatForm


def select_date(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    halls = Hall.objects.filter(movie__slug=movie_slug)

    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            selected_seats = form.cleaned_data['seat']
            for seat in selected_seats:
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
        'halls': halls,
    }

    return render(request, 'theater/select_date.html', context=context)


def buy_ticket_hall(request, movie_slug, hall_slug):
    hall = Hall.objects.get(slug=hall_slug)
    movie = get_object_or_404(Movie, slug=movie_slug)
    seats = Seat.objects.filter(hall__slug=hall_slug)
    halls = Hall.objects.filter(movie__slug=movie_slug)

    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            # selected_seats = form.cleaned_data['seat']
            # for seat in selected_seats:
            #     seat_movies = Seat.objects.filter(
            #         hall__slug=hall_slug, number=seat.number)
            #     for seat_movie in seat_movies:
            #         seat_movie.user = request.user
            #         seat_movie.is_available = False
            #         seat_movie.save()
            return redirect('confirmation', movie_slug, hall_slug)

    else:
        form = SeatForm()

    context = {
        'movie': movie,
        'form': form,
        'seats': seats,
        'hall': hall,
        'halls': halls,
    }

    return render(request, 'theater/buy_ticket.html', context=context)
