Este mini proyecto se compone de dos partes:

1.- Una parte se encarga de generar un conjunto de codigos QR, y se puede usar de manera independiete. Un vez generado los codigos QR los almacena en una BBDD de SQLite con el Usuario al que ha sido asignado el Token que pertence al QR generado.

2.- Otra parte que se encarga de mediante camara, registrar la lectura del QR y almacenar el registro en otra BBDD de SQLite en donde se podra observar por fecha y hora cual ha sido el Token que ha validado a traves de la lectura del QR mediante la camara.

En el fichero requirements.txt se encontran las diferentes librerias necesarias para la ejecucion del proyecto.
Para la instalacion del fichero requirements.txt utilizar el comando: pip install -r requirements.txt

Se recomienda crear un entorno de desarrollo para una mejor ejecucion, puede utilizar el comando python -m virtualenv venv para crear un entorno de desarrollo. Primero debera instalar la libreria virtualenv si no la tiene instalada mediante el comando pip install virtualenv.