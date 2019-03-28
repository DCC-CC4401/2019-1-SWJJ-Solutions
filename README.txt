Instrucciones para ejecutar.

Nota: Se sugiere fuertemente crear un ambiente virtual para ejecutar el proyecto.

Se requiere al menos Python 3.6. para ejecutar el proyecto, con Python 2.7 es esperable que no se pueda ejecutar nada.
Este proyecto es solamente referencial, no es la verdad absoluta y existen mas y mejores formas de hacer ciertas cosas.

En este proyecto en honor al tiempo se usaron ciertas malas practicas, las que seran comentadas en el foro de U-Cursos.
Cualquier duda, problema o consulta, preguntar por el foro del curso, yo o cualquier otra persona que sepa, los ayudaran.
--------------------------------------------------------------------------------------------------------------------------
comandos entorno virtual

python3 -m venv mi-entorno-virtual

source mi-entorno-virtual/bin/activate
--------------------------------------------------------------------------------------------------------------------------
Comandos (deben ser ejecutados en el orden presentado):

pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver
--------------------------------------------------------------------------------------------------------------------------

Espero les sea de ayuda este proyecto.
Pablo Miranda Á.
