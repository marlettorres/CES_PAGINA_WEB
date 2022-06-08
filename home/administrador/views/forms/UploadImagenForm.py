from django import forms
from home.models import PaginaCecyte, ImagenNoticia,ContenidoPagina
from django.contrib.auth.models import User
import datetime

def guardar_archivo(tipo,carpeta, file):   
    fecha=datetime.datetime.now()
    archivo=file.name
    extension=archivo.split('.')[-1]
    nombre=tipo+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension
    #with open(f"recursos/{carpeta}{file.name}", "wb+") as destination:
    with open(f"recursos/{carpeta}{nombre}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

class UploadImagenForm(forms.Form):
    imagenes = forms.FileField(required=True)
    contenido_pagina_id = forms.IntegerField()
    #def formulario_valido(self, request):
        #form_valido = True
        #if self.is_valid() == False:
            #form_valido = False
        #return form_valido 
        
    def guardar_imagen_bd(self, request, id):
        fecha=datetime.datetime.now()
        contenido = ImagenNoticia()
        archivo=request.FILES["archivo_imagen"].name
        extension=archivo.split('.')[-1]
        contenido.imagenes= 'Slider'+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension
        contenido.contenido_pagina_id = id
        contenido.save()

    def guardar_imagen_disco(self, request):
        pagina_cecyte = PaginaCecyte.objects.get(id=6)
        guardar_archivo('Slider',pagina_cecyte.carpeta, request.FILES["archivo_imagen"])
