from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'studio', 'cat', 'start_rental', 'end_rental', 'released')
    list_display_links = ('id', 'name')
    list_editable = ('start_rental', 'end_rental', 'released')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)