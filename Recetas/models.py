from django.db import models

from Usuarios.models import Usuarios
from Ingredientes.models import Ingrediente


# Create your models here.

class Receta(models.Model):
  Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  nombre = models.CharField(max_length=50)
  ingrediente1 = models.ForeignKey(Ingrediente,
                                   on_delete=models.CASCADE,
                                   related_name='primer_ingrediente')
  ingrediente2 = models.ForeignKey(Ingrediente,
                                   on_delete=models.CASCADE,
                                   related_name='segundo_ingrediente')
  ingrediente3 = models.ForeignKey(Ingrediente,
                                   on_delete=models.CASCADE,
                                   related_name='tercer_ingrediente',
                                   blank=True,
                                   null=True)
  ingrediente4 = models.ForeignKey(Ingrediente,
                                   on_delete=models.CASCADE,
                                   related_name='cuarto_ingrediente',
                                   blank=True,
                                   null=True)
  preparacion = models.CharField(max_length=2000)

  def __str__(self):
    return self.nombre


class RecetaPicture(models.Model):
  Receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='receta/')

  def __str__(self):
    return f'{self.Receta.nombre} -- {str(self.imagen)}'
