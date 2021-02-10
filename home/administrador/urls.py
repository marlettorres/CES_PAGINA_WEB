from django.contrib import admin
from django.urls import path

from .views import avisos_agregar_view, avisos_view, inicio_view, login_view

urlpatterns = [
    path("administrador", inicio_view, name="admin-inicio"),
    path("administrador/login", login_view, name="admin-login"),
    path("administrador/avisos", avisos_view, name="admin-avisos"),
    path(
        "administrador/avisos/agregar", avisos_agregar_view, name="admin-avisos-agregar"
    ),
    path(
        "administrador/avisos/editar/<int:id>",
        avisos_agregar_view,
        name="admin-avisos-editar",
    ),
]
