from django import forms
from .models import Seat


class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['row', 'seat']