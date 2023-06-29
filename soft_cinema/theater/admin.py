from django.contrib import admin
from .models import Seat, Hall


class HallAdmin(admin.ModelAdmin):
    exclude = ['slug']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        for seat in range(1, 33):
            hall_seat = Seat(hall=obj, number=seat)
            hall_seat.save()




admin.site.register(Seat)
admin.site.register(Hall, HallAdmin)
