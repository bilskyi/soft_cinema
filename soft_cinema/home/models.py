from django.db import models
from django.urls import reverse

class Movie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    poster = models.ImageField(upload_to='posters/')
    age_limit = models.PositiveIntegerField()
    year = models.PositiveIntegerField(verbose_name='Released date') #year of production
    original_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    start_rental = models.DateField()  
    end_rental = models.DateField()
    cat = models.ManyToManyField('Category')
    language = models.CharField(max_length=255)
    duration = models.DurationField()
    production = models.CharField(max_length=255) #country
    studio = models.CharField(max_length=255)
    starring = models.TextField()
    description = models.TextField()
    released = models.BooleanField()
   

    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Category / Genre'
        verbose_name_plural = 'Categories / Genres'
