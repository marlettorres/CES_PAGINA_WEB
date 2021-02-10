from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.models import PaginaCecyte, ContenidoPagina


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


@login_required(login_url="/administrador/login")
def avisos_view(request):
    if request.method == "POST":
        return POST_RESPONSE(request)
    return GET_RESPONSE(request)