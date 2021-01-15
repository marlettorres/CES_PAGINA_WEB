from django.shortcuts import render
from home.models import Estado


def cecyte_view(request):
    estados = Estado.objects.filter(estatus=True)
    context = {"estados": estados}
    return render(request, "cecyte/cecyte.html", context)
