from django.contrib import admin
from django.urls import path

from home.views_.indicadores import indicadores_view

urlpatterns = [
    path('indicadores', indicadores_view, name="indicadores"),
]
