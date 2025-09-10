from django.urls import path #Imports the path function to define URL patterns
from . import views #Imports views from the current app

urlpatterns = [
    path('', views.home, name='home'),
    path('login-mainpage/', views.loginmain, name='login-mainpage'),
    path('signup-mainpage/', views.signupmain, name='singup-mainpage'),
    path('signup-librarian/', views.signup_librarian, name='signup-librarian'),
    path('librarian_list/', views.librarian_search, name='librarian_list'),
]