from django.contrib import admin
from django.urls import path

from home.views_.inicio import inicio_view

urlpatterns = [
    path("", inicio_view, name="inicio"),
]
