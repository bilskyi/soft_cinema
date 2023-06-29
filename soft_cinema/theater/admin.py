from django.contrib import admin
from .models import Seat, Hall, HallSeat


class HallAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        seats = Seat.objects.all()

        for seat in seats:
            hall_seat = HallSeat(hall=obj, seat=seat)
            hall_seat.save()




admin.site.register(Seat)
admin.site.register(Hall, HallAdmin)
admin.site.register(HallSeat)
