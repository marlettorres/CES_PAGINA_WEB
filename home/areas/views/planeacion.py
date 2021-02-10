from django.shortcuts import render

from .shared import get_contenido_area


def planeacion_view(request):
    context = get_contenido_area(3)
    return render(request, "areas/planeacion.html", context)
