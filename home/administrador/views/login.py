from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render


def GET_RESPONSE(request, context={}):
    return render(request, "administrador/login.html", context)


def POST_RESPONSE(request):
    context = {
        "username": request.POST["usuario"],
        "password": request.POST["password"],
    }

    user = authenticate(
        request,
        username=context["username"],
        password=context["password"],
    )

    if user is None:
        context["error"] = "Usuario y/o contraseña incorrecto"
        return GET_RESPONSE(request, context)

    login(request, user)
    return HttpResponseRedirect("/administrador")


def login_view(request):
    if request.method == "POST":
        return POST_RESPONSE(request)
    return GET_RESPONSE(request)
