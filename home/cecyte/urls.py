from django.contrib import admin
from django.urls import path
from .views import cecyte_view, cecyte_planteles, informacion_planteles

urlpatterns = [
    path("cecytes", cecyte_view, name="cecytes"),
    path("cecyte/planteles/<int:id>", cecyte_planteles, name="cecyte/planteles/"),
    path(
        "informacion/planteles/<int:id>/<int:idpe>",
        informacion_planteles,
        name="informacion/planteles/",
    ),
]