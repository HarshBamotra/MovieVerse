from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view()),
    path('movies/', MoviesPage.as_view(), name='movies'),
    path('offers/', OffersPage.as_view(), name='offers'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('movie/<int:movie_id>/', MoviePage.as_view()),
    path('booking/<int:movie_id>/', BookingPage.as_view()),
    path('confirm_booking/<int:movie_id>/', confirm_booking),

]