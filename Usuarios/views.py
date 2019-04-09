from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from Usuarios.models import Usuarios
from Usuarios.models import ProfilePicture
from Usuarios.forms import RegistroUsuarioForm

from Ingredientes.models import Ingrediente
from Ingredientes.models import IngredientePicture

from Recetas.models import Receta
from Recetas.models import RecetaPicture


# Create your views here.

def inicio_sesion(request):
    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            usuario = Usuarios.objects.get(User=user)

            return HttpResponseRedirect(reverse('usuarios:perfil', kwargs={'usuario_id': usuario.id}))

    logout(request)

    return render(request, 'Usuarios/UsuariosLanding.html', {})


def perfil_usuario(request, usuario_id):
    usuario = Usuarios.objects.get(pk=usuario_id)
    imagen = ProfilePicture.objects.filter(Usuario_id=usuario_id).first()

    ingredientes = Ingrediente.objects.filter(Usuario=usuario)[:3]
    ingredients_list = []
    for ingrediente in ingredientes:
        imagen = IngredientePicture.objects.get(ingrediente=ingrediente)
        ingredients_list.append((ingrediente, imagen))

    recetas = Receta.objects.filter(Usuario=usuario)[:3]
    recetas_list = []
    for receta in recetas:
        imagen = RecetaPicture.objects.get(Receta=receta)
        recetas_list.append((receta, imagen))

    return render(request, 'Usuarios/Perfil.html',
                  {'usuario': usuario, 'imagen': imagen, 'ingredientes': ingredients_list, 'recetas': recetas_list})


def registrar_usuario(request):
    if request.POST:
        form = RegistroUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, new_user)

            usuario = Usuarios.objects.get(User=new_user)

        return HttpResponseRedirect(reverse('usuarios:perfil', kwargs={'usuario_id': usuario.id}))

    form = RegistroUsuarioForm()

    return render(request, 'Usuarios/Registro.html', {'register_form': form})


def cerrar_sesion(request):
    logout(request)

    return HttpResponseRedirect(reverse('usuarios:inicio'))


def menuPrincipalAdmin(request):
    return render(request, 'Usuarios/loginFake.html')


def homeAdmin(request):
    return render(request,'Menu/home.html')

def resumenEvaluacion(request):
    return render(request,'Menu/resumenEvaluacion.html')

def eval(request):
    return render(request,'Menu/eval.html')

def generadorDeRubrica(request):
    return render(request,'Menu/generadorDeRubrica.html')

def evaluaciones(request):
    return render(request,'Menu/evaluaciones.html')

def evaluaEvaluador(request):
    return render(request,'Menu/evaluaEvaluador.html')