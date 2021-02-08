from django.shortcuts import render
from home.models import (
    Estado,
    CatPlanteles,
    EncuestaPlantel,
    PlantelInformacion,
    PlantelInfraestructura,
    PlantelEstadistica,
    PlantelEscolaridad,
    OfertaEducativa,
    PlantelLegal,
    PlantelVinculacion,
)


def cecyte_view(request):
    estados = Estado.objects.filter(estatus=True)
    context = {"estados": estados}
    return render(request, "cecyte/cecyte.html", context)


def cecyte_planteles(request, id):
    planteles = CatPlanteles.objects.filter(estado_id=id)
    print("planteles", planteles)
    context = {"planteles": planteles}
    return render(request, "cecyte/detalle/filtro_plantel.html", context)


def informacion_planteles(request, id):
    context = {}
    encuesta = EncuestaPlantel.objects.filter(plantel_id=id).first()
    encuesta_id = 0
    if encuesta is not None:
        encuesta_id = encuesta.id

    informacion = PlantelInformacion.objects.filter(encuesta_id=encuesta_id).first()
    infraestructura = PlantelInfraestructura.objects.filter(
        encuesta_id=encuesta_id
    ).first()
    estadistica = PlantelEstadistica.objects.filter(encuesta_id=encuesta_id).first()
    escolaridad = PlantelEscolaridad.objects.filter(encuesta_id=encuesta_id).first()
    oferta = OfertaEducativa.objects.filter(encuesta_id=encuesta_id)
    legal = PlantelLegal.objects.filter(encuesta_id=encuesta_id).first()
    vinculacion = PlantelVinculacion.objects.filter(encuesta_id=encuesta_id).first()

    context = {
        "encuesta": encuesta,
        "informacion": informacion,
        "infraestructura": infraestructura,
        "estadistica": estadistica,
        "escolaridad": escolaridad,
        "oferta": oferta,
        "legal": legal,
        "vinculacion": vinculacion,
    }
    return render(request, "cecyte/detalle/informacion.html", context)
