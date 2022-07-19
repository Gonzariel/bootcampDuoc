from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path
from MusicApp import views


urlpatterns = [
    path('', views.index, name='INDEX'),
]