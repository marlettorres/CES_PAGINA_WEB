from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from home.forms import UploadFileForm
from home.models import PaginaCecyte, ContenidoPagina


def guardar_archivo(carpeta: str, file):
    with open(f"recursos/{carpeta}{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def guardar_archivos(form: UploadFileForm, request):
    tipo_bloque = form.cleaned_data["tipo_bloque"]
    pagina_cecyte = PaginaCecyte.objects.get(id=form.cleaned_data["pagina_cecyte_id"])
    guardar_archivo(pagina_cecyte.carpeta, request.FILES["archivo_vista"])
    if tipo_bloque == 2:  # pdf
        guardar_archivo(pagina_cecyte.carpeta, request.FILES["pdf"])
    if tipo_bloque == 3:  # imagen
        guardar_archivo(pagina_cecyte.carpeta, request.FILES["imagen"])


def guardar_aviso(form: UploadFileForm, request):
    tipo_bloque = form.cleaned_data["tipo_bloque"]

    contenido = ContenidoPagina(
        nombre=form.cleaned_data["nombre"],
        archivo_vista=request.FILES["archivo_vista"].name,
        pagina_cecyte_id=form.cleaned_data["pagina_cecyte_id"],
    )
    if tipo_bloque == 1:  # texto
        contenido.texto = form.cleaned_data["texto"]
    if tipo_bloque == 2:  # pdf
        contenido.pdf = request.FILES["pdf"].name
    if tipo_bloque == 3:  # imagen
        contenido.imagen = request.FILES["imagen"].name

    contenido.save()
    guardar_archivos(form, request)


def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            context["error"] = "Usuario y/o contraseña incorrecto"

    return render(request, "administrador/login.html", context)


def aviso_validar(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid() == False:
        return False

    tipo_bloque = form.cleaned_data["tipo_bloque"]
    valido = True
    if tipo_bloque == 1 and "texto" not in request.POST is None:  # texto
        valido = False

    elif tipo_bloque == 2 and "pdf" not in request.FILES:  # pdf
        valido = False

    elif tipo_bloque == 3 and "imagen" not in request.FILES:  # imagen
        valido = False
    return valido


@login_required(login_url="/administrador/login")
def aviso_agregar_view(request: HttpRequest, id=None):
    context = {"paginas_cecyte": PaginaCecyte.objects.all()}
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if aviso_validar(request):
            guardar_aviso(form, request)
            return HttpResponseRedirect("/administrador/inicio")
        else:
            context["form"] = form
            context["error"] = "Favor de llenar correctamente el formulario"

    if id is not None:
        aviso = ContenidoPagina.objects.get(id=id)
        form = UploadFileForm()
        form.nombre = aviso.nombre
        context["form"] = UploadFileForm()
    return render(request, "administrador/avisos_agregar.html", context)


@login_required(login_url="/administrador/login")
def inicio_view(request):
    context = {}
    return render(request, "administrador/inicio.html", context)


@login_required(login_url="/administrador/login")
def aviso_lista_view(request):
    secciones = PaginaCecyte.objects.all()
    context = {"secciones": secciones}
    form = {}
    pagina_cecyte_id = request.GET.get("seccion_id", None)
    estatus = request.GET.get("estatus", None)

    if pagina_cecyte_id is not None:
        pagina_cecyte = PaginaCecyte.objects.get(id=pagina_cecyte_id)
        avisos = pagina_cecyte.get_contenido()
        if estatus == "1":
            avisos = avisos.filter(estatus=True)
        elif estatus == "0":
            avisos = avisos.filter(estatus=False)
        form["estatus"] = estatus
        form["seccion_id"] = int(pagina_cecyte_id)

        context["avisos"] = avisos
        context["ruta"] = pagina_cecyte.carpeta
        context["form"] = form

    return render(request, "administrador/avisos.html", context)