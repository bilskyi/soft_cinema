from django.contrib import admin
from .models import Seat, Hall

class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_number', 'is_available']
    list_display_links = list_display


class HallAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        seats = Seat.objects.all()

        for seat in seats:
            seat.hall.add(obj)

admin.site.register(Seat)
admin.site.register(Hall, HallAdmin)
