from django.shortcuts import render
from home.models import AreaCoordinacion


def directorio_coordinacion_view(request):
    areas_coordinacion = AreaCoordinacion.objects.filter(estatus=True)
    context = {"areas_coordinacion": areas_coordinacion}
    return render(request, "directorio/coordinacion.html", context)
