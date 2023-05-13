from django.contrib import admin
from .models import Seat

class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_number', 'is_available', 'movie']
    list_display_links = list_display


admin.site.register(Seat, SeatAdmin)