from django import forms

from Usuarios.models import Usuarios
from Usuarios.models import ProfilePicture


class RegistroUsuarioForm(forms.Form):
  foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),
                          required=True,
                          label="Imagen de Perfil")
  nombre = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           required=True)
  app_paterno = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=True,
                                label='Apelido Paterno')
  app_materno = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=False,
                                label='Apellido Materno')
  username = forms.CharField(max_length=20,
                             widget=forms.TextInput(attrs={'class': 'form-control'}),
                             required=True,
                             label='Nombre de usuario')
  password = forms.CharField(max_length=25,
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                             required=True,
                             label='Contraseña')

  def is_valid(self):
    return super(RegistroUsuarioForm, self).is_valid()

  def save(self, *args, **kwargs):
    user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    user.first_name = self.cleaned_data['nombre']
    user.last_name = self.cleaned_data['app_paterno']
    user.save()

    usuario = Usuarios(User=user, app_materno=self.cleaned_data['app_materno'])
    usuario.save()

    imagen_perfil = ProfilePicture(Usuario=usuario, imagen=self.cleaned_data['foto'])
    imagen_perfil.save()
    
    return user

