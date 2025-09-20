from django.urls import path #Imports the path function to define URL patterns
from . import views #Imports views from the current app

urlpatterns = [
    path('', views.home, name='home'),
    path('signup-mainpage/', views.signupmain, name='signup-mainpage'),
    path('login-mainpage/', views.loginmain, name='login-mainpage'),
    path('signup-librarian/', views.signup_librarian, name='signup-librarian'),
    path('signup-library-member/', views.signup_library_member, name='signup-library-member'),
    path('librarian_list/', views.librarian_search, name='librarian_list'),
]