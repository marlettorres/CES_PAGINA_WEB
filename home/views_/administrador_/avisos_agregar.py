from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render

from home.forms import UploadFileForm
from home.models import PaginaCecyte, ContenidoPagina


def GET_RESPONSE(request, context, id=None):
    if id is not None:
        contenido = ContenidoPagina.objects.get(id=id)
        form = UploadFileForm()
        form.nombre = contenido.nombre
        form.pagina_cecyte_id = contenido.pagina_cecyte.id
        context["form"] = UploadFileForm()

    return render(request, "administrador/avisos_agregar.html", context)


def guardar_archivo(carpeta, file):
    with open(f"recursos/{carpeta}{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def validar_formulario(form, request):
    form_valido = True
    if form.is_valid() == False:
        form_valido = False
    tipo_bloque = form.cleaned_data["tipo_bloque"]
    if tipo_bloque == 1 and "texto" not in request.POST is None:  # texto
        form_valido = False
    elif tipo_bloque == 2 and "pdf" not in request.FILES:  # pdf
        form_valido = False
    elif tipo_bloque == 3 and "imagen" not in request.FILES:  # imagen
        form_valido = False
    return form_valido


def guardar_avisos_bd(form, request, id):

    tipo_bloque = form.cleaned_data["tipo_bloque"]
    if id is not None:
        contenido = ContenidoPagina.objects.get(id=id)
    else:
        contenido = ContenidoPagina()

    contenido["nombre"] = form.cleaned_data["nombre"]
    contenido["archivo_vista"] = request.FILES["archivo_vista"].name
    contenido["pagina_cecyte_id"] = form.cleaned_data["pagina_cecyte_id"]

    if tipo_bloque == 1:  # texto
        contenido.texto = form.cleaned_data["texto"]
    if tipo_bloque == 2:  # pdf
        contenido.pdf = request.FILES["pdf"].name
    if tipo_bloque == 3:  # imagen
        contenido.imagen = request.FILES["imagen"].name
    contenido.save()


def guardar_avisos_disco(form, request):
    tipo_bloque = form.cleaned_data["tipo_bloque"]
    pagina_cecyte_id = form.cleaned_data["pagina_cecyte_id"]

    pagina_cecyte = PaginaCecyte.objects.get(id=pagina_cecyte_id)
    guardar_archivo(pagina_cecyte.carpeta, request.FILES["archivo_vista"])
    if tipo_bloque == 2:  # pdf
        guardar_archivo(pagina_cecyte.carpeta, request.FILES["pdf"])
    if tipo_bloque == 3:  # imagen
        guardar_archivo(pagina_cecyte.carpeta, request.FILES["imagen"])


def POST_RESPONSE(request, id):
    context = {}
    form = UploadFileForm(request.POST, request.FILES)

    form_valido = validar_formulario(form, request)
    if form_valido == False:
        context["error"] = "Favor de llenar correctamente el formulario"
        return GET_RESPONSE(request, context)

    guardar_avisos_bd(form, request, id)
    guardar_avisos_disco(form, request)

    return HttpResponseRedirect("/administrador/avisos")


@login_required(login_url="/administrador/login")
def avisos_agregar_view(request, id=None):
    context = {
        "paginas_cecyte": PaginaCecyte.objects.all(),
    }
    if request.method == "POST":
        return POST_RESPONSE(request, id)
    return GET_RESPONSE(request, context, id)