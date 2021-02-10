from django.shortcuts import render

from .shared import get_contenido_area


def vinculacion_view(request):
    context = get_contenido_area(2)
    return render(request, "areas/vinculacion.html", context)
