from django.contrib import admin
from django.urls import path

from .views import avisos_agregar_view, avisos_view, inicio_view, login_view, registrousuario_view, actualizar_usuario,eliminar_usuario, modificar_usuario,salir,cambiar_estado

urlpatterns = [
    path("administrador", inicio_view, name="admin-inicio"),
    path("administrador/salir", salir, name="admin-salir"),
    path("administrador/login", login_view, name="admin-login"),
    path("administrador/avisos", avisos_view, name="admin-avisos"),
    path("administrador/registrousuario", registrousuario_view, name="admin-usuario"),
    path("administrador/nuevo-usuario", registrousuario_view, name="admin-nuevo-usuario"),
    path("administrador/modificar-usuario", modificar_usuario, name="admin-modificar-usuario"),
    path(
        "administrador/actualizar-usuario/<int:id>",
         actualizar_usuario, 
         name="admin-actualizar-usuario"),
    path(
        "administrador/eliminar-usuario/<int:id>",
         eliminar_usuario, 
         name="admin-eliminar-usuario"),
    path(
        "administrador/avisos/agregar", avisos_agregar_view, name="admin-avisos-agregar"
    ),
    path(
        "administrador/avisos/editar/<int:id>",
        avisos_agregar_view,
        name="admin-avisos-editar",
    ),
    path(
        "administrador/avisos/cambiar-estado/<int:id>",
        cambiar_estado,
        name="admin-cambiar-estado",
    ),
]
