from django.contrib import admin
from django.urls import path

# from home.views_.administrador import   inicio_view,  aviso_lista_view, aviso_agregar_view
from home.views_.administrador_.login import  login_view
from home.views_.administrador_.inicio import  inicio_view
from home.views_.administrador_.avisos import  avisos_view
from home.views_.administrador_.avisos_agregar import  avisos_agregar_view

urlpatterns = [
    path("administrador", inicio_view, name="admin-inicio"),
    path("administrador/login", login_view, name="admin-login"),
    path("administrador/avisos", avisos_view, name="admin-avisos"),
    path("administrador/avisos/agregar", avisos_agregar_view, name="admin-avisos-agregar"),
    path("administrador/avisos/editar/<int:id>", avisos_agregar_view, name="admin-avisos-editar"),
]
