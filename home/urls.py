from django.contrib import admin
from django.urls import path

from home.urls_.cecyte import urlpatterns as cecyte_urls
from home.urls_.areas import urlpatterns as areas_urls
from home.urls_.emsad import urlpatterns as emsad_urls
from home.urls_.directorio import urlpatterns as directorio_urls
from home.urls_.indicadores import urlpatterns as indicadores_urls
from home.urls_.misionyvision import urlpatterns as misionyvision_urls
from home.urls_.ofertaeducativa import urlpatterns as ofertaeducativa_urls
from home.urls_.inicio import urlpatterns as inicio_urls
from home.urls_.administrador import urlpatterns as administrador_urls

appname = "home"

urlpatterns = []
urlpatterns += cecyte_urls
urlpatterns += areas_urls
urlpatterns += emsad_urls
urlpatterns += directorio_urls
urlpatterns += indicadores_urls
urlpatterns += misionyvision_urls
urlpatterns += ofertaeducativa_urls
urlpatterns += inicio_urls
urlpatterns += administrador_urls
