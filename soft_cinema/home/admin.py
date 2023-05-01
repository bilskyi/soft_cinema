from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'studio', 'start_rental', 'end_rental']
    list_display_links = ['id', 'name']
    filter_horizontal = ['cat', 'state']
    list_editable = ['start_rental', 'end_rental']
    prepopulated_fields = {'slug': ['name']}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ['name']}


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'stage']
    list_display_links = ['id', 'stage']
    prepopulated_fields = {'slug': ['stage']}

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(State, StateAdmin)