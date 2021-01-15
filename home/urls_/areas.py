from django.contrib import admin
from django.urls import path

from home.views_.areas import finanzas_view, planeacion_view, academica_view, vinculacion_view, normatividad_view, informatica_view

appname = "home"

urlpatterns = [
    path('areas/finanzas', finanzas_view, name="area-finanzas"),
    path('areas/planeacion', planeacion_view, name="area-planeacion"),
    path('areas/academica', academica_view, name="area-academica"),
    path('areas/vinculacion', vinculacion_view, name="area-vinculacion"),
    path('areas/normatividad', normatividad_view, name="area-normatividad"),
    path('areas/informatica', informatica_view, name="area-informatica"),
]
