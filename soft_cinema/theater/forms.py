from django import forms
from .models import HallSeat

class SeatForm(forms.Form):
    seat = forms.ModelMultipleChoiceField(
        queryset=HallSeat.objects.filter(is_available=True),
        widget=forms.CheckboxSelectMultiple,
    )