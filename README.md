# Create and Read User Code QR
Este proyecto permite la creación y lectura de códigos QR asignados a usuarios, utilizando tecnologías web y bases de datos SQLite. Se divide en dos componentes principales.

> [!IMPORTANT]
Este proyecto es de caracter educativo y sirve para entender conceptos basicos relacionados al uso de aplicaciones WEB y la creacion y lecturad de codigos QR.

## Funcionalidad
### Generación de Códigos QR:
1. Genera códigos QR y los asocia con usuarios específicos.
2. Guarda los códigos QR y la información del usuario en una base de datos SQLite.
3. Acepta datos a través de archivos CSV o Excel. Los tokens pueden ser asignados a usuarios o generados aleatoriamente.

### Lectura de Códigos QR:
1. Utiliza una cámara web para leer códigos QR.
2. Almacena registros de lectura en otra base de datos SQLite, incluyendo detalles como fecha, hora y token validado.

## Creacion del entorno de virtual:
python -m virtualenv nombreEntorno

## Dependencias
pip freeze > requirements.txt  
pip install -r requirements.txt

> [!TIP]
Se recomienda la creación de un entorno virtual para optimizar el desarrollo y la ejecución del proyecto.

> [!NOTE]
Dentro de los ficheros se encuentran dos BBDD creadas en SQLite donde se almacena la informacion que se lee y crea sobre los diferentes codigos QR, estan ubicadas dentro de src/database/.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor haz un 'fork' del repositorio, crea una rama con tus mejoras y envía un 'pull request'.

## Licencia
Este proyecto está bajo una licencia MIT. Consulta el archivo LICENSE para más detalles.
