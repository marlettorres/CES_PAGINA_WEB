from django.shortcuts import render

from .shared import get_contenido_area


def informatica_view(request):
    context = get_contenido_area(7)
    return render(request, "areas/informatica.html", context)
