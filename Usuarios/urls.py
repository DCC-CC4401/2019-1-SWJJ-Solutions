from django.urls import path

from Usuarios.views import inicio_sesion
from Usuarios.views import perfil_usuario
from Usuarios.views import registrar_usuario
from Usuarios.views import cerrar_sesion

from Usuarios.views import menuPrincipalAdmin

urlpatterns = [
  path('', inicio_sesion, name='inicio'),
  path('registro', registrar_usuario, name='registro'),
  path('perfil/<int:usuario_id>/', perfil_usuario, name='perfil'),
  path('logout/', cerrar_sesion, name='logout'),

  path('menuPrincipal/', menuPrincipalAdmin, name='menuAdmin'),
]
