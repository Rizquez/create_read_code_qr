# Create and Read User Code QR

## USO
Este proyecto se compone de dos partes independientes explicadas a continuacion:

1. Una parte se encarga de generar un conjunto de codigos QR, y se puede usar de manera independiete. Un vez generado los codigos QR los almacena en una BBDD de SQLite con el Usuario al que ha sido asignado el Token que pertence al QR generado.

2. Otra parte que se encarga de mediante camara WEB, registrar la lectura del QR y almacenar el registro en otra BBDD de SQLite en donde se podra observar por fecha y hora cual ha sido el Token que ha validado a traves de la lectura del QR mediante la camara.

La entrada de los datos para la creacion de los codigos QR se realiza mediante un fichero CSV o un fichero Excel. Es posible asginar un Token a cada Usuario y por consiguiente la generacion del QR sera directamente sobre el Token asignado, de lo contrario se generara un Token aleatorio que previamente sera asignado a cada usuario antes de la generacion del QR.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor haz un 'fork' del repositorio, crea una rama con tus mejoras y envía un 'pull request'.

## Licencia
Este proyecto está bajo una licencia MIT. Consulta el archivo LICENSE para más detalles.

## Creacion del entorno de virtual:
python -m virtualenv nombreEntorno

## Dependencias
pip freeze > requirements.txt  
pip install -r requirements.txt

> [!NOTE]
Dentro de los ficheros se encuentran dos BBDD creadas en SQLite donde se almacena la informacion que se lee y crea sobre los diferentes codigos QR, estan ubicadas dentro de src/database/.

> [!TIP]
Se recomienda crear un entorno virtual para un optimo desarrollo y ejecucion ejecucion.

> [!IMPORTANT]
Este proyecto es de caracter educativo y sirve para entender conceptos basicos relacionados al uso de aplicaciones WEB y la creacion y lecturad de codigos QR.
