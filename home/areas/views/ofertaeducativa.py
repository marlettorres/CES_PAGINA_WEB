from django.shortcuts import render
from home.models import OfertaEducativaArea, OfertaEducativaCarrera


def ofertaeducativa_view(request):
    areas = OfertaEducativaArea.objects.filter(estatus=True)
    context = {"areas_educativas": areas}
    return render(request, "ofertaeducativa/ofertaeducativa.html", context)