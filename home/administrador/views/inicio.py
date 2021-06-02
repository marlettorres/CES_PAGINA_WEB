from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def GET_RESPONSE(request, context={}):
    return render(request, "administrador/inicio.html", context)


def POST_RESPONSE(request):
    context = {}
    return GET_RESPONSE(request, context)

def salir(request):
    logout(request)
    return redirect(to="/administrador")

@login_required(login_url="/administrador/login")
def inicio_view(request):
    if request.method == "POST":
        return POST_RESPONSE(request)
    return GET_RESPONSE(request)