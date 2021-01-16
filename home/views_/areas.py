from django.shortcuts import render

from home.models import ContenidoPagina, PaginaCecyte


def finanzas_view(request):
    context = {}
    return render(request, "areas/finanzas.html", context)


def planeacion_view(request):
    context = get_contenido_area(3)
    return render(request, "areas/planeacion.html", context)


def academica_view(request):
    context = get_contenido_area(1)
    return render(request, "areas/academica.html", context)


def vinculacion_view(request):
    context = get_contenido_area(2)
    return render(request, "areas/vinculacion.html", context)


def informatica_view(request):
    context = get_contenido_area(7)
    return render(request, "areas/informatica.html", context)


def normatividad_view(request):
    context = {}
    return render(request, "areas/normatividad.html", context)


def get_contenido_area(id):
    pagina_cecyte = PaginaCecyte.objects.get(id=id)
    elementos = ContenidoPagina.objects.filter(
        pagina_cecyte=pagina_cecyte,
        estatus=1,
    )

    return {
        "pagina_cecyte": pagina_cecyte,
        "ruta": pagina_cecyte.carpeta,
        "elementos": elementos,
    }
