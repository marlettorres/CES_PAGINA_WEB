from django import forms
from home.models import PaginaCecyte, ContenidoPagina


def guardar_archivo(carpeta, file):
    with open(f"recursos/{carpeta}{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class UploadFileForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    archivo_vista = forms.FileField()
    texto = forms.CharField(max_length=1000, required=False)
    pdf = forms.FileField(required=False)
    imagen = forms.FileField(required=False)
    pagina_cecyte_id = forms.IntegerField()
    tipo_bloque = forms.IntegerField()

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

        if id is not None:
            contenido = ContenidoPagina.objects.get(id=id)
        else:
            contenido = ContenidoPagina()
        print("self.cleaned_data['nombre']", self.cleaned_data["nombre"])
        contenido.nombre = self.cleaned_data["nombre"]
        contenido.archivo_vista = request.FILES["archivo_vista"].name
        contenido.pagina_cecyte_id = self.cleaned_data["pagina_cecyte_id"]

        if tipo_bloque == 1:  # texto
            contenido.texto = self.cleaned_data["texto"]
        if tipo_bloque == 2:  # pdf
            contenido.pdf = request.FILES["pdf"].name
        if tipo_bloque == 3:  # imagen
            contenido.imagen = request.FILES["imagen"].name
        contenido.save()

    def guardar_avisos_disco(self, request):
        tipo_bloque = self.cleaned_data["tipo_bloque"]
        pagina_cecyte_id = self.cleaned_data["pagina_cecyte_id"]

        pagina_cecyte = PaginaCecyte.objects.get(id=pagina_cecyte_id)
        guardar_archivo(pagina_cecyte.carpeta, request.FILES["archivo_vista"])
        if tipo_bloque == 2:  # pdf
            guardar_archivo(pagina_cecyte.carpeta, request.FILES["pdf"])
        if tipo_bloque == 3:  # imagen
            guardar_archivo(pagina_cecyte.carpeta, request.FILES["imagen"])
