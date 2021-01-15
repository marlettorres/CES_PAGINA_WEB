from django.contrib import admin
from django.urls import path

from home.views_.administrador import login_view,  inicio_view,  aviso_lista_view, aviso_agregar_view

urlpatterns = [
    path("administrador", inicio_view, name="admin-inicio"),
    path("administrador/login", login_view, name="admin-login"),
    path("administrador/avisos", aviso_lista_view, name="admin-paginas"),
    path("administrador/avisos/agregar", aviso_agregar_view, name="admin-paginas-editar"),
    path("administrador/avisos/editar/<int:id>", aviso_agregar_view, name="admin-paginas-editar"),
]
