from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view()),
    path('movies/', MoviesPage.as_view()),
    path('offers/', OffersPage.as_view()),
    path('signup/', SignupPage.as_view()),
    path('login/', LoginPage.as_view()),
    path('logout/', user_logout),
    path('movie/<int:movie_id>/', MoviePage.as_view()),
    path('booking/<int:movie_id>/', BookingPage.as_view()),
    path('confirm_booking/<int:movie_id>/', confirm_booking),

]