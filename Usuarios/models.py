from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
  User = models.ForeignKey(User, on_delete=models.CASCADE)
  app_materno = models.CharField(max_length=50, blank=True, null=True)
  produce_contenido = models.BooleanField(default=False)
  numero_recetas = models.IntegerField(default=0)

  def __str__(self):
    return f'{self.User.first_name} {self.User.last_name} {self.app_materno}'


class ProfilePicture(models.Model):
  Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='profile/')

  def __str__(self):
    return f'{str(self.usuario)} -- {str(self.imagen)}'