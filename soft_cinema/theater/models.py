from django.db import models
from django.contrib import admin
from home.models import Movie
from user.models import Profile
from django.utils.text import slugify


class Seat(models.Model):
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, null=True)
    number = models.PositiveSmallIntegerField()
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

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.movie} - {self.date}"


    def save(self, *args, **kwargs):
        original_slug = slugify(f"{self.movie}-{self.date}")
        unique_slug = original_slug
        counter = 1

        while Hall.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{counter}"
            counter += 1

        self.slug = unique_slug
        super().save(*args, **kwargs)