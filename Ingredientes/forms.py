from django import forms

from Ingredientes.models import Ingrediente
from Ingredientes.models import IngredientePicture

class AddIngredienteForm(forms.Form):
  usuario_id = forms.IntegerField(widget=forms.HiddenInput())
  foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),
                          required=True,
                          label="Imagen del Ingrediente")
  nombre = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           required=True)
  descripcion = forms.CharField(max_length=2000,
                                widget=forms.Textarea(
                                  attrs={'class': 'form-control',
                                         'rows': '4'}
                                ),
                                required=True)

  def is_valid(self):
    return super(AddIngredienteForm, self).is_valid()

  def save(self, *args, **kwargs):
    ingrediente = Ingrediente(Usuario_id=self.cleaned_data['usuario_id'],
                              nombre=self.cleaned_data['nombre'],
                              descripcion=self.cleaned_data['descripcion'])
    ingrediente.save()

    imagen=IngredientePicture(ingrediente=ingrediente, imagen=self.cleaned_data['foto'])
    imagen.save()
     