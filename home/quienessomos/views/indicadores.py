from django.shortcuts import render


def indicadores_view(request):
    context = {}
    return render(request, "indicadores/indicadores.html", context)
