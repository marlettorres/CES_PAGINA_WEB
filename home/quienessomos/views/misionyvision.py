from django.shortcuts import render

from home.models import MisionYVision


def misionyvision_view(request):
    data = MisionYVision.objects.first()
    context = {
        "mision": data.mision,
        "vision": data.vision,
    }
    return render(request, "misionyvision/misionyvision.html", context)