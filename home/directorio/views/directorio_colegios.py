from django.shortcuts import render
from home.models import PersonaColegio


def directorio_colegios_view(request):
    colegios = PersonaColegio.objects.filter(estatus=True)
    context = {"colegios": colegios}
    return render(request, "directorio/colegios.html", context)
