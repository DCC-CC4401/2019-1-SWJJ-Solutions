from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Ingredientes.models import Ingrediente
from Ingredientes.models import IngredientePicture
from Recetas.models import Receta
from Recetas.models import RecetaPicture
from Recetas.forms import AddRecetaForm
from Usuarios.models import Usuarios
from Usuarios.models import ProfilePicture

# Create your views here.


def all_reciepes(request):
  usuario = Usuarios.objects.get(User=request.user)
  imagen = ProfilePicture.objects.filter(Usuario=usuario).first()
  recetas = Receta.objects.all()
  recetas_list = []

  for receta in recetas:
    imagen = RecetaPicture.objects.get(Receta=receta)
    recetas_list.append((receta, imagen))

  form = AddRecetaForm(initial={'usuario_id': usuario.id})

  return render(request, 'Recetas/List.html', {'recetas': recetas_list, 'usuario': usuario, 'imagen': imagen, 'form': form})


def add_receta(request):
  if request.POST:
    form = AddRecetaForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()

  return HttpResponseRedirect(reverse('recetas:list'))


def delete_receta(request, receta_id):
  RecetaPicture.objects.get(Receta_id=receta_id).delete()
  Receta.objects.get(pk=receta_id).delete()

  return HttpResponseRedirect(reverse('recetas:list'))



def detalles_receta(request, receta_id):
  usuario = Usuarios.objects.get(User=request.user)
  imagen = ProfilePicture.objects.filter(Usuario=usuario).first()
  receta = Receta.objects.get(pk=receta_id)
  receta_imagen = RecetaPicture.objects.get(Receta_id=receta_id)

  return render(request, 'Recetas/detalles.html', {'usuario': usuario, 'imagen': imagen, 'receta': receta, 'receta_pic': receta_imagen})
