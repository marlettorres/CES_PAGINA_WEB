from django.contrib import admin
from django.urls import path


from .views import indicadores_view, misionyvision_view

urlpatterns = [
    path("indicadores", indicadores_view, name="indicadores"),
    path("misionyvision", misionyvision_view, name="misionyvision"),
]
