from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    poster = models.ImageField(upload_to='posters/')
    age_limit = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    original_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    start_rental = models.DateField()  
    end_rental = models.DateField()  
    language = models.CharField(max_length=255)
    duration = models.DurationField()
    production = models.CharField(max_length=255)
    studio = models.CharField(max_length=255)
    starring = models.TextField()
    description = models.TextField()
    released = models.BooleanField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    
    def __str__(self) -> str:
        return self.name