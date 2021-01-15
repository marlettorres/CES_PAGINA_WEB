from django.contrib import admin
from django.urls import path

from home.views_.ofertaeducativa import ofertaeducativa_view

appname = "home"

urlpatterns = [
    path('ofertaeducativa', ofertaeducativa_view, name="oferta-educativa"),
]
