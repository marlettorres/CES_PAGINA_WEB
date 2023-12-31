from django import forms
from home.models import PaginaCecyte, ContenidoPagina
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

def guardar_video(tipo, file):   
    fecha=datetime.datetime.now()
    archivo=file.name
    extension=archivo.split('.')[-1]
    nombre=tipo+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension
    #with open(f"recursos/{carpeta}{file.name}", "wb+") as destination: 
    with open(f"media/{nombre}", "wb+") as destination: 
        for chunk in file.chunks():
            destination.write(chunk) 

class UploadFileForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion_breve = forms.CharField(max_length=1000, required=False)
    archivo_vista = forms.FileField()
    texto = forms.CharField(max_length=5000, required=False)
    pdf = forms.FileField(required=False)
    imagen = forms.FileField(required=False)
    pagina_cecyte_id = forms.IntegerField()
    tipo_bloque = forms.IntegerField()
    video = forms.FileField(max_length=500, required=False)
    opcion_video=forms.IntegerField(required=False)

    def formulario_valido(self, request):
        form_valido = True
        if self.is_valid() == False:
            form_valido = False
        tipo_bloque = self.cleaned_data["tipo_bloque"]
        if tipo_bloque == 1 and "texto" not in request.POST:  # texto
            form_valido = False
        elif tipo_bloque == 2 and "pdf" not in request.FILES:  # pdf
            form_valido = False
        elif tipo_bloque == 3 and "imagen" not in request.FILES:  # imagen
            form_valido = False
        return form_valido

    def guardar_avisos_bd(self, request, id): 
        tipo_bloque = self.cleaned_data["tipo_bloque"]
        tipo_opcion = self.cleaned_data["opcion_video"]
        fecha=datetime.datetime.now()

        if id is not None:
            contenido = ContenidoPagina.objects.get(id=id)
        else:
            contenido = ContenidoPagina()
        #print("self.cleaned_data['nombre']", self.cleaned_data["nombre"])
        contenido.nombre = self.cleaned_data["nombre"]
        contenido.descripcion_breve = self.cleaned_data["descripcion_breve"]
        #contenido.archivo_vista = request.FILES["archivo_vista"].name
        archivo=request.FILES["archivo_vista"].name
        extension=archivo.split('.')[-1]
        contenido.archivo_vista = 'Cu'+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension
        contenido.pagina_cecyte_id = self.cleaned_data["pagina_cecyte_id"]
        contenido.estatus="1"
        if tipo_opcion == 1:
            contenido.video=''
            contenido.opcion_video=1
        elif tipo_opcion ==2:
            archivo_video=request.FILES["video"].name   
            extension_video=archivo_video.split('.')[-1]
            contenido.video = 'Video'+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension_video
            contenido.opcion_video=2
        elif tipo_opcion ==3:
            contenido.video=request.POST["liga"]
            contenido.opcion_video=3 
        #if 'video' not in request.FILES:
        #    contenido.video=''
        #else: 
        #    archivo_video=request.FILES["video"].name   
        #    extension_video=archivo_video.split('.')[-1]
        #    contenido.video = 'Video'+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension_video

        if tipo_bloque == 1:  # texto
            contenido.texto = self.cleaned_data["texto"]
            contenido.pdf=''
            contenido.imagen=''
        if tipo_bloque == 2:  # pdf
            archivo=request.FILES["pdf"].name
            extension=archivo.split('.')[-1]
            #contenido.pdf = request.FILES["pdf"].name
            contenido.pdf = 'Pdf'+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension
            contenido.texto=''
            contenido.imagen=''
        if tipo_bloque == 3:  # imagen
            archivo=request.FILES["imagen"].name
            extension=archivo.split('.')[-1]
            #contenido.imagen = request.FILES["imagen"].name
            contenido.imagen = 'Img'+fecha.strftime('%d.%m.%Y-%H.%M.%S.')+extension
            contenido.texto=''
            contenido.pdf=''
        contenido.save()

    def guardar_avisos_disco(self, request):
        tipo_bloque = self.cleaned_data["tipo_bloque"]
        pagina_cecyte_id = self.cleaned_data["pagina_cecyte_id"]

        pagina_cecyte = PaginaCecyte.objects.get(id=pagina_cecyte_id)
        guardar_archivo('Cu',pagina_cecyte.carpeta, request.FILES["archivo_vista"])
        tipo_video = self.cleaned_data["opcion_video"]
        if tipo_video == 2:
            guardar_video('Video', request.FILES["video"])
        #if "video" in request.FILES:
        #    guardar_archivo('Video',pagina_cecyte.carpeta, request.FILES["video"])
        if tipo_bloque == 2:  # pdf
            guardar_archivo('Pdf',pagina_cecyte.carpeta, request.FILES["pdf"])
        if tipo_bloque == 3:  # imagen
            guardar_archivo('Img',pagina_cecyte.carpeta, request.FILES["imagen"])


class Usuarionuevo(forms.ModelForm):
    
    class Meta:
       model = User
       fields=["username","password"]

   # username= forms.CharField(max_length=150)
    #password=forms.CharField(max_length=128)

    #def guardar_usuario_bd(request):
       # contenido =User
