from django.shortcuts import render

from .shared import get_contenido_area


def academica_view(request):
    context = get_contenido_area(1)
    return render(request, "areas/academica.html", context)
