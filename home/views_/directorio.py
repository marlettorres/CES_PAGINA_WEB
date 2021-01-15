from django.shortcuts import render
from home.models import AreaCoordinacion, PersonaCoordinacion, PersonaColegio


def directorio_coordinacion_view(request):
    areas_coordinacion = AreaCoordinacion.objects.filter(estatus=True)
    context = {"areas_coordinacion": areas_coordinacion}
    return render(request, "directorio/coordinacion.html", context)


def directorio_colegios_view(request):
    colegios = PersonaColegio.objects.filter(estatus=True)
    context = {"colegios": colegios}
    return render(request, "directorio/colegios.html", context)
