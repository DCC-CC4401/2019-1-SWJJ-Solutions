from django import forms

from Ingredientes.models import Ingrediente
from Recetas.models import Receta
from Recetas.models import RecetaPicture

class AddRecetaForm(forms.Form):
  usuario_id = forms.IntegerField(widget=forms.HiddenInput())
  foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),
                          required=True,
                          label="Imagen de la Receta")
  nombre = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           required=True)
  ingrediente1 = forms.ModelChoiceField(queryset=Ingrediente.objects,
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        required=True,
                                        label='Primer Ingrediente')
  ingrediente2 = forms.ModelChoiceField(queryset=Ingrediente.objects,
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        required=True,
                                        label='Segundo Ingrediente')
  ingrediente3 = forms.ModelChoiceField(queryset=Ingrediente.objects,
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        required=False,
                                        label='Tercer Ingrediente')
  ingrediente4 = forms.ModelChoiceField(queryset=Ingrediente.objects,
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        required=False,
                                        label='Cuarto Ingrediente')
  preparacion = forms.CharField(max_length=2000,
                                  widget=forms.Textarea(
                                    attrs={'class': 'form-control',
                                           'rows': '6'}
                                  ),
                                  required=True,
                                  label='Preparación')

  def is_valid(self):
    return super(AddRecetaForm, self).is_valid()

  def save(self, *args, **kwargs):
    receta = Receta(Usuario_id=self.cleaned_data['usuario_id'],
                    nombre=self.cleaned_data['nombre'],
                    ingrediente1=self.cleaned_data['ingrediente1'],
                    ingrediente2=self.cleaned_data['ingrediente2'],
                    ingrediente3=self.cleaned_data['ingrediente3'],
                    ingrediente4=self.cleaned_data['ingrediente4'],
                    preparacion=self.cleaned_data['preparacion'])
    receta.save()

    imagen = RecetaPicture(Receta=receta, imagen=self.cleaned_data['foto'])
    imagen.save()
