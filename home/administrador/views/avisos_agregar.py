from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from home.models import PaginaCecyte

from .forms import UploadFileForm


def GET_RESPONSE(request, context, id=None):
    form = UploadFileForm()
    if id is not None:
        contenido = ContenidoPagina.objects.get(id=id)
        form.nombre = contenido.nombre
        form.pagina_cecyte_id = contenido.pagina_cecyte.id
    context["form"] = form

    return render(request, "administrador/avisos_agregar.html", context)


def POST_RESPONSE(request, id):
    context = {}
    form = UploadFileForm(request.POST, request.FILES)

    form_valido = form.formulario_valido(request)
    if form_valido == False:
        context["error"] = "Favor de llenar correctamente el formulario"
        return GET_RESPONSE(request, context)

    form.guardar_avisos_bd(request, id)
    form.guardar_avisos_disco(request)

    return HttpResponseRedirect("/administrador/avisos")


@login_required(login_url="/administrador/login")
def avisos_agregar_view(request, id=None):
    context = {
        "paginas_cecyte": PaginaCecyte.objects.all(),
    }
    if request.method == "POST":
        return POST_RESPONSE(request, id)
    return GET_RESPONSE(request, context, id)