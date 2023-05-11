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
    form = SeatForm()
    context = {
        'movie': movie,
        'form': form,
    }
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('movies')
    return render(request, 'theater/buy_ticket.html', context=context)