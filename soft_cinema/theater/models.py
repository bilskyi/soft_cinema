from django.db import models


class Seat(models.Model):
    seat_number = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.seat_number