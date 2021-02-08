from django.shortcuts import render
from home.models import Estado,CatPlanteles,EncuestaPlantel,PlantelInformacion,PlantelInfraestructura,PlantelEstadistica,PlantelEscolaridad,OfertaEducativa,PlantelLegal,PlantelVinculacion


def cecyte_view(request):
    estados = Estado.objects.filter(estatus=True)
    planteles =[]
    context = {"estados": estados, "planteles": planteles}
    return render(request, "cecyte/cecyte.html", context)

def cecyte_planteles(request, id):    
    planteles = CatPlanteles.objects.filter(estado_id=id)
    context = {"planteles": planteles}
    return render(request, "cecyte/detalle_cecyte_plantel.html", context)

def informacion_planteles(request, id):    
    encuesta = EncuestaPlantel.objects.filter(plantel_id=id).first()
    informacion = {}
    if encuesta is not None:
        informacion = PlantelInformacion.objects.filter(encuesta_id=encuesta.id).first()
        if informacion is None:
            informacion = {}
            
        infraestructura = PlantelInfraestructura.objects.filter(encuesta_id=encuesta.id).first()
        if infraestructura is None:
            infraestructura = {}

        estadistica = PlantelEstadistica.objects.filter(encuesta_id=encuesta.id).first()
        if estadistica is None:
            estadistica = {}

        escolaridad = PlantelEscolaridad.objects.filter(encuesta_id=encuesta.id).first()
        if escolaridad is None:
            escolaridad = {}

        oferta = OfertaEducativa.objects.filter(encuesta_id=encuesta.id).first()
        if oferta is None:
            oferta = {}

        legal = PlantelLegal.objects.filter(encuesta_id=encuesta.id).first()
        if legal is None:
            legal = {}

        vinculacion = PlantelVinculacion.objects.filter(encuesta_id=encuesta.id).first()
        if vinculacion is None:
            vinculacion = {}

    context = {"informacion": informacion, "infraestructura":infraestructura, "estadistica":estadistica, "escolaridad":escolaridad, "oferta":oferta, "legal":legal, "vinculacion":vinculacion}
    return render(request, "cecyte/mostrar_informacion.html", context)
