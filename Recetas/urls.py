from django.urls import path

from Recetas.views import all_reciepes
from Recetas.views import add_receta
from Recetas.views import delete_receta
from Recetas.views import detalles_receta

urlpatterns = [
    path('', all_reciepes, name='list'),
    path('add/', add_receta, name='add'),
    path('delete/<int:receta_id>', delete_receta, name='delete'),
    path('receta/<int:receta_id>', detalles_receta, name='details')
]
