from django.contrib import admin
from django.urls import path
from .views import emsad_view 

urlpatterns = [
    path("emsad", emsad_view, name="emsad"),
]
