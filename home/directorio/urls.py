from django.contrib import admin
from django.urls import path

from .views import (
    directorio_colegios_view,
    directorio_coordinacion_view,
)

urlpatterns = [
    path(
        "directorio/coordinacion",
        directorio_coordinacion_view,
        name="directorio-coordinacion",
    ),
    path("directorio/colegios", directorio_colegios_view, name="directorio-colegios"),
]
