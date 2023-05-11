from django import forms
from .models import Seat


class SeatForm(forms.Form):
    seat = forms.ModelChoiceField(queryset=Seat.objects.filter(is_available=True))
    