# Create Read Code QR

Este mini proyecto se compone de dos partes:

1.- Una parte se encarga de generar un conjunto de codigos QR, y se puede usar de manera independiete. Un vez generado los codigos QR los almacena en una BBDD de SQLite con el Usuario al que ha sido asignado el Token que pertence al QR generado.

2.- Otra parte que se encarga de mediante camara, registrar la lectura del QR y almacenar el registro en otra BBDD de SQLite en donde se podra observar por fecha y hora cual ha sido el Token que ha validado a traves de la lectura del QR mediante la camara.

En el fichero requirements.txt se encontran las diferentes librerias necesarias para la ejecucion del proyecto.

Se recomienda crear un entorno de desarrollo para una mejor ejecucion.

## Creacion del entorno de desarrollo:
python -m virtualenv nombreEntorno

## Creacion o instalacion archivo requirements.txt
pip freeze > requirements.txt  
pip install -r requirements.txt
