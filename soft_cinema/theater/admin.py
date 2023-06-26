from django.contrib import admin
from .models import Seat, Hall

class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_number', 'is_available']
    list_display_links = list_display


class HallAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['movie']}


admin.site.register(Seat)
admin.site.register(Hall, HallAdmin)