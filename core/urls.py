from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login-mainpage/', views.loginmain, name='login-mainpage'),
    path('signup-mainpage/', views.signupmain, name='singup-mainpage'),
    path('signup-librarian/', views.signup_librarian, name='signup-librarian'),
    path('librarian_list/', views.librarian_search, name='librarian_list'),
]