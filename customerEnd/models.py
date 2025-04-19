from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

class Movies(models.Model):
    name = models.CharField(max_length=512)
    poster = models.ImageField(upload_to='posters/')
    category = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    trailer = models.URLField()
    status = models.CharField(max_length=10, choices=[('showing', "Now Showing"), ('upcoming', "Upcoming Releases")])
    release_date = models.DateField()
    language = models.CharField(max_length=256, default='English')
    duration = models.DurationField(default=timedelta(hours=2))


class Offers(models.Model):
    title = models.CharField(max_length=512)
    category = models.CharField(max_length=256)
    image = models.ImageField(upload_to='offers/')
    description = models.CharField(max_length=256)
    offer_added = models.DateTimeField(auto_now_add=True)



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    show_date = models.DateField()
    show_time = models.TimeField()
    seats = models.CharField(max_length=100)
    booked_at = models.DateTimeField(auto_now_add=True)
