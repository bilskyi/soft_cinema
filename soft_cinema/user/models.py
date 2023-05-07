from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.username