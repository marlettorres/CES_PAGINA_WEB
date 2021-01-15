from django.contrib import admin
from django.urls import path

from home.views_.directorio import directorio_coordinacion_view, directorio_colegios_view

urlpatterns = [
    path('directorio/coordinacion',
         directorio_coordinacion_view,
         name="directorio-coordinacion"),
    path('directorio/colegios',
         directorio_colegios_view,
         name="directorio-colegios"),
]
