from django.shortcuts import render

def finanzas_view(request):
    context = {}
    return render(request, "areas/finanzas.html", context)
