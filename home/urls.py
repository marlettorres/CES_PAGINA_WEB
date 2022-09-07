from django.contrib import admin
from django.urls import path

from .areas import urlpatterns as areas_urls
from .administrador import urlpatterns as administrador_urls
from .directorio import urlpatterns as directorio_urls
from .quienessomos import urlpatterns as quienessomos_urls
from .emsad import urlpatterns as emsad_urls
from .inicio import urlpatterns as inicio_urls
from .cecyte import urlpatterns as cecyte_urls

appname = "home"

urlpatterns = []
urlpatterns += areas_urls
urlpatterns += administrador_urls
urlpatterns += directorio_urls
urlpatterns += quienessomos_urls
urlpatterns += emsad_urls
urlpatterns += cecyte_urls
urlpatterns += inicio_urls


