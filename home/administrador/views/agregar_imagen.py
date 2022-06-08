from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from home.models import PaginaCecyte
from home.models import ContenidoPagina
from home.models import ImagenNoticia
from .forms import UploadImagenForm

def GET_RESPONSE(request, context, id=None):
    form = UploadImagenForm()
    if id is not None:
        contenido = ContenidoPagina.objects.get(id=id)
        contenido2 = PaginaCecyte.objects.all()
        form.nombre = contenido.nombre
        form.pagina_cecyte_id = contenido.pagina_cecyte.id
        context={"form" : form,
        "idd":contenido.id,
        "nom":contenido.nombre,
        "paginas_cecyte":contenido2,
        "paginas_cecyte2":contenido.pagina_cecyte,
        }
        
        return render(request, "administrador/agregar_imagen.html", context)
    context["form"] = form

    return render(request, "administrador/agregar_imagen.html", context)


def POST_RESPONSE(request, id):
    context = {}
    form = UploadImagenForm(request.POST, request.FILES)
    
    #form_valido = form.formulario_valido(request)
    #if form.is_valid():
        #context["error"] = "Favor de llenar correctamente el formulario"
        #return GET_RESPONSE(request, context)

    if form.is_valid():
        context["success"] = "Guardado correctamente"
    form.guardar_imagen_bd(request, id)
    form.guardar_imagen_disco(request)

    return HttpResponseRedirect("/administrador/avisos")


@login_required(login_url="/administrador/login")
def agregar_imagen_view(request, id=None):
    context = {
        "paginas_cecyte": PaginaCecyte.objects.all(),
    }
    if request.method == "POST":
        return POST_RESPONSE(request, id)
    return GET_RESPONSE(request, context, id)