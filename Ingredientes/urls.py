from django.urls import path

from Ingredientes.views import all_ingredients
from Ingredientes.views import add_ingredient
from Ingredientes.views import delete_ingredient
from Ingredientes.views import detalles_ingrediente

urlpatterns = [
    path('', all_ingredients, name='list'),
    path('add/', add_ingredient, name='add'),
    path('delete/<int:ingrediente_id>', delete_ingredient, name='delete'),
    path('ingrediente/<int:ingrediente_id>', detalles_ingrediente, name='details')
]
