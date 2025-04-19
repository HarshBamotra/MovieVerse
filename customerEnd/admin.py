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


class BookingAdmin(admin.ModelAdmin):
    search_fields = ["user", "get_movie_title"]
    list_display = ["full_name", "get_movie_title", "email", "phone", "seats", "booked_at"]
    list_filter = ["user"]

    def get_movie_title(self, obj):
        return obj.movie.name  


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Offers, OffersAdmin)
admin.site.register(Booking, BookingAdmin)

