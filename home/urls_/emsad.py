from django.contrib import admin
from django.urls import path

from home.views_.emsad import emsad_view

urlpatterns = [
    path('emsad', emsad_view, name="emsad"),
]
