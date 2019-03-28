from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Ingredientes.models import Ingrediente
from Ingredientes.models import IngredientePicture
from Ingredientes.forms import AddIngredienteForm
from Usuarios.models import Usuarios
from Usuarios.models import ProfilePicture

# Create your views here.

def all_ingredients(request):
  usuario = Usuarios.objects.get(User=request.user)
  imagen = ProfilePicture.objects.filter(Usuario=usuario).first()
  ingredientes = Ingrediente.objects.all()
  ingredients_list = []

  for ingrediente in ingredientes:
    imagen = IngredientePicture.objects.get(ingrediente=ingrediente)
    ingredients_list.append((ingrediente, imagen))

  form = AddIngredienteForm(initial={'usuario_id': usuario.id})

  return render(request, 'Ingredientes/List.html', {'ingredientes': ingredients_list, 'usuario': usuario, 'imagen': imagen, 'form': form})


def add_ingredient(request):
  if request.POST:
    form = AddIngredienteForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()

  return HttpResponseRedirect(reverse('Ingredientes:list'))

def delete_ingredient(request, ingrediente_id):
  IngredientePicture.objects.get(ingrediente_id=ingrediente_id).delete()
  Ingrediente.objects.get(pk=ingrediente_id).delete()

  return HttpResponseRedirect(reverse('Ingredientes:list'))


def detalles_ingrediente(request, ingrediente_id):
  usuario = Usuarios.objects.get(User=request.user)
  imagen = ProfilePicture.objects.filter(Usuario=usuario).first()
  ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
  ingrediente_imagen = IngredientePicture.objects.get(ingrediente_id=ingrediente_id)

  return render(request, 'Ingredientes/detalles.html', {'usuario': usuario, 'imagen': imagen, 'ingrediente': ingrediente, 'ingr_pic': ingrediente_imagen})
