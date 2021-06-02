from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from home.models import PaginaCecyte, ContenidoPagina
import os

def GET_RESPONSE(request, context={}):
    secciones = PaginaCecyte.objects.all()
    context = {"secciones": secciones}
    form = {}

    pagina_cecyte_id = request.GET.get("seccion_id", None)
    estatus = request.GET.get("estatus", None)
    if pagina_cecyte_id is not None:
        pagina_cecyte = PaginaCecyte.objects.get(id=pagina_cecyte_id)
        avisos = ContenidoPagina.objects.filter(pagina_cecyte=pagina_cecyte)
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


def POST_RESPONSE(request):
    context = {}
    return GET_RESPONSE(request, context)

def cambiar_estado(request,id):
    aviso = ContenidoPagina.objects.get(id=id)
    aviso.estatus='0'
    
    url=PaginaCecyte.objects.get(id=aviso.pagina_cecyte_id)
    if aviso.archivo_vista is not None:
        os.remove("recursos/"+url.carpeta+aviso.archivo_vista)
        aviso.archivo_vista=''
    #if aviso.pdf is not None:
    if len(aviso.pdf) > 2:    
        os.remove("recursos/"+url.carpeta+aviso.pdf)
        aviso.pdf=''
    #elif aviso.imagen is not None:
    elif len(aviso.imagen) > 2:
        os.remove("recursos/"+url.carpeta+aviso.imagen)
        aviso.imagen=''
   
    aviso.save()
    return redirect(to="/administrador/avisos")

@login_required(login_url="/administrador/login")
def avisos_view(request):
    if request.method == "POST":
        return POST_RESPONSE(request)
    return GET_RESPONSE(request)