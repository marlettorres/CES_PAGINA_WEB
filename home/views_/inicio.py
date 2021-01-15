from django.shortcuts import render



def inicio_view(request):
    context = { }
    return render(request, "inicio/inicio.html", context)
