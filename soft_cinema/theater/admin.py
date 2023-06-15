from django.contrib import admin
from .models import Seat, SeatMovie

class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_number', 'is_available']
    list_display_links = list_display


class SeatMovieAdmin(admin.ModelAdmin):
    list_display = ['seat', 'movie', 'is_available']
    list_display_links = list_display

admin.site.register(Seat, SeatAdmin)
admin.site.register(SeatMovie, SeatMovieAdmin)