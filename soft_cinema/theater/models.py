from django.db import models
from home.models import Movie


class Seat(models.Model):
    seat_number = models.PositiveSmallIntegerField(unique=True)
    is_available = models.BooleanField(default=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f'Seat number {self.seat_number}'