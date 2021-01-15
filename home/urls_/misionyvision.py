from django.contrib import admin
from django.urls import path

from home.views_.misionyvision import misionyvision_view

urlpatterns = [
    path('misionyvision', misionyvision_view, name="misionyvision"),
]
