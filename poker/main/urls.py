"""Defines URL patterns for the main body of the app"""

from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    #Include default auth urls
    path('', include('django.contrib.auth.urls')),

    #Home page
    path('', views.index, name='index'),

    #Registration page
    path('register/', views.register, name='register'),
]