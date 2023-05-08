from django.db import models


class Seat(models.Model):
    row = models.CharField(max_length=1)
    seat = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Row {self.row}, Seat {self.seat}, Available: {self.available}"