from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import Usuarionuevo

def GET_RESPONSE(request):
    context ={
        'usuarios': User.objects.all()
    }
    return render(request, "administrador/usuario.html", context)

def  POST_RESPONSE(request):
    if request.method == 'POST':
        nombre=request.POST.get('username')
        us = User.objects.filter(username=nombre).count()
        if us == 1:
            return redirect(to="/administrador/registrousuario")
        else:
            user = User.objects.create_user(request.POST.get('username'), ' ', request.POST.get('password'))
    return redirect(to="/administrador/registrousuario")

def actualizar_usuario(request, id):
    usuario= User.objects.get(id=id)
    context = { 
        'usuarios': User.objects.all(),
        'usuario': usuario
    }
    
    return render(request, "administrador/usuario.html", context)

def modificar_usuario(request):
    if request.method == 'POST':
        idd=request.POST.get('iduser')
        usuarnom=request.POST.get('username')
        us=User.objects.exclude(id=idd).filter(username=usuarnom).count()
        if us == 1:
            return redirect(to="/administrador/registrousuario")
        else:
            user = User.objects.get(id=idd)
            user.username = request.POST.get('username')
            #user.password = request.POST.get('password')
            user.set_password(request.POST.get('password'))
            user.save()
    return redirect(to="/administrador/registrousuario")

def eliminar_usuario(request, id):
    usuario= User.objects.get(id=id)
    usuario.delete()
    return redirect(to="/administrador/registrousuario")

@login_required(login_url="/administrador/login")
def registrousuario_view(request):
    if request.method == "POST":
        return POST_RESPONSE(request)
    return GET_RESPONSE(request)