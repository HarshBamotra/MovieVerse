from django.contrib import admin
from .models import *


class MoviesAdmin(admin.ModelAdmin):
    search_fields = ["name", "category"]
    list_display = ["name", "category", "status", "release_date"]
    list_filter = ["name", "category"]


class OffersAdmin(admin.ModelAdmin):
    search_fields = ["title", "category"]
    list_display = ["title", "category"]
    list_filter = ["title", "category"]


admin.site.register(Booking)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Offers, OffersAdmin)

