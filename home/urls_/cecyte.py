from django.contrib import admin
from django.urls import path

from home.views_.cecyte import cecyte_view

urlpatterns = [
    path('cecytes', cecyte_view, name="cecytes"),
]
