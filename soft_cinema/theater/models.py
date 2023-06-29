from django.db import models
from django.contrib import admin
from home.models import Movie
from user.models import Profile
from django.utils.text import slugify


class Seat(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"{self.number} - {self.user}"


class Hall(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()
    slug = models.SlugField(db_index=True, unique=True, blank=True)

    def __str__(self):
        return f"{self.movie} - {self.date}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.movie}-{self.date}")
        super().save(*args, **kwargs)


class HallSeat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
