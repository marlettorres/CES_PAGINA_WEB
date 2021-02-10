from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def GET_RESPONSE(request, context={}):
    return render(request, "administrador/inicio.html", context)


def POST_RESPONSE(request):
    context = {}
    return GET_RESPONSE(request, context)


@login_required(login_url="/administrador/login")
def inicio_view(request):
    if request.method == "POST":
        return POST_RESPONSE(request)
    return GET_RESPONSE(request)