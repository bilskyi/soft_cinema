from django import forms
from .models import Seat

class SeatForm(forms.Form):
    seat = forms.ModelMultipleChoiceField(
        queryset=Seat.objects.filter(is_available=True),
        widget=forms.CheckboxSelectMultiple,
    )