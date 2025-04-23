from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


class HomePage(TemplateView):
    template_name = 'customerEnd/home.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):

        showing_movies = Movies.objects.filter(status='showing').order_by("-release_date")
        if len(showing_movies) > 4 and len(showing_movies) < 8:
            showing_movies = showing_movies[:4]
        elif len(showing_movies) > 8:
            showing_movies = showing_movies[:8]

        upcoming_movies = Movies.objects.filter(status='upcoming').order_by("-release_date")
        if len(upcoming_movies) > 4 and len(upcoming_movies) < 8:
            upcoming_movies = upcoming_movies[:4]
        elif len(upcoming_movies) > 8:
            upcoming_movies = upcoming_movies[:8]

        self.extra_context = {"showing_movies": showing_movies, "upcoming_movies": upcoming_movies}
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class MoviesPage(TemplateView):
    template_name = 'customerEnd/movies.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):

        showing_movies = Movies.objects.filter(status='showing').order_by("-release_date")
        upcoming_movies = Movies.objects.filter(status='upcoming').order_by("-release_date")

        self.extra_context = {"showing_movies": showing_movies, "upcoming_movies": upcoming_movies}
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class OffersPage(TemplateView):
    template_name = 'customerEnd/offers.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        offers = Offers.objects.all().order_by("-offer_added")

        self.extra_context = {"offers": offers}
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class SignupPage(TemplateView):
    template_name = 'customerEnd/signup.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        self.extra_context = {"offers": 'test'}
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm_password"]

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created! Please log in.")
        return redirect("login")
    

class LoginPage(TemplateView):
    template_name = 'customerEnd/login.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")
        

def user_logout(request):
    logout(request)
    return redirect('/')

class MoviePage(TemplateView):
    template_name = 'customerEnd/movie.html'
    extra_context = {}

    def get(self, request, movie_id, *args, **kwargs):
        movie = get_object_or_404(Movies, id=movie_id)
        self.extra_context = {'movie': movie}
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class BookingPage(TemplateView):
    template_name = 'customerEnd/book.html'
    extra_context = {}

    def get(self, request, movie_id, *args, **kwargs):
        movie = get_object_or_404(Movies, id=movie_id)
        self.extra_context = {'movie': movie}
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        

def confirm_booking(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        no_of_seats = request.POST.get('seats')
        payment_mothod = request.POST.get('payment_method')

        # Optional: get show_date, time, seats from frontend or pre-filled values
        show_date = '2025-04-28'  # example static
        show_time = '18:30:00'    # 6:30 PM in 24-hour format
        seats = 'A4, A5'          # sample seats

        booking = Booking.objects.create(
            user=request.user if request.user.is_authenticated else None,
            movie=movie,
            full_name=full_name,
            email=email,
            phone=phone,
            show_date=show_date,
            show_time=show_time,
            seats=seats,
            numseats = no_of_seats,
            payment_mothod = payment_mothod
        )
        return render(request, 'customerEnd/bookingConfirm.html', {'booking': booking})

    return redirect('movies')



