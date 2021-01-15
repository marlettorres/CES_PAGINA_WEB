from django.shortcuts import render


def emsad_view(request):
    context = {}
    return render(request, "emsad/emsad.html", context)
