from django.db import models
from home.models import Movie

class Seat(models.Model):
    seat_number = models.PositiveSmallIntegerField(unique=True)
    is_available = models.BooleanField(default=True)
    movies = models.ManyToManyField(Movie, through='SeatMovie')

    def __str__(self):
        return f'Seat number {self.seat_number}'

class SeatMovie(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Seat {self.seat} - Movie {self.movie}'
