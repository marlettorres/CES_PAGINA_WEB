from django.shortcuts import render


def normatividad_view(request):
    context = {}
    return render(request, "areas/normatividad.html", context)
