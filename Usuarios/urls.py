from django.urls import path

from Usuarios.views import inicio_sesion
from Usuarios.views import perfil_usuario
from Usuarios.views import registrar_usuario
from Usuarios.views import cerrar_sesion

from Usuarios.views import menuPrincipalAdmin
from Usuarios.views import homeAdmin
from Usuarios.views import resumenEvaluacion

from Usuarios.views import eval
from Usuarios.views import generadorDeRubrica
urlpatterns = [
  path('', inicio_sesion, name='inicio'),
  path('registro', registrar_usuario, name='registro'),
  path('perfil/<int:usuario_id>/', perfil_usuario, name='perfil'),
  path('logout/', cerrar_sesion, name='logout'),

  path('menuPrincipal/', menuPrincipalAdmin, name='menuAdmin'),
  path('homeAdmin/', homeAdmin, name='homeAdmin'),
  path('resumenEvaluacion/', resumenEvaluacion, name='resumenEvaluacion'),
  path('eval/', eval, name='eval'),
  path('generadorDeRubrica/', generadorDeRubrica, name='generadorDeRubrica'),

]
