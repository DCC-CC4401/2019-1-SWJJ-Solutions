from django.db import models

from Usuarios.models import Usuarios
# Create your models here.

class Ingrediente(models.Model):
  Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  nombre = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=2000)

  def __str__(self):
    return self.nombre


class IngredientePicture(models.Model):
  ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='ingrediente/')

  def __str__(self):
    return f'{str(self.ingrediente)} -- {str(self.imagen)}'
