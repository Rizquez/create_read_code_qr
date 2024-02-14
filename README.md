# Create and Read User Code QR
Este proyecto permite la creación y lectura de códigos QR asignados a usuarios, utilizando tecnologías web y Flask como Framework de desarrollo y como SGBD a SQLite. Se divide en dos componentes principales.

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

3. ## Estructura del proyecto
```
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
├── src
│   ├── database
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── existing_qr.db
│   │   └── registros.db
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   └── utils
│       ├── __init__.py
│       └── functions.py
└── templates
    └── index.html
```

## Creacion del entorno de virtual:
Se necesitara tener instalada previamente la libreria 'virtualenv', en caso contrario se podra instalar ejecutando el siguiente comando:
```
pip install virtualenv
```
Una vez instalada, para crear un entorno de desarrollo se debe ejecutar:
```
python -m virtualenv venv
```

> [!TIP]
Se recomienda la creación de un entorno virtual para optimizar el desarrollo y la ejecución del proyecto.

## Dependencias
Este comando instala las dependencias necesarias sobre este proyecto:
```
pip install -r requirements.txt
```
Y este comando crea o actualiza el archivo txt que almacena las dependencias del proyecto:
```
pip freeze > requirements.txt  
```

> [!NOTE]
Dentro de los ficheros se encuentran dos BBDD creadas en SQLite donde se almacena la informacion que se lee y crea sobre los diferentes codigos QR, estan ubicadas dentro de src/database/.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor haz un 'fork' del repositorio, crea una rama con tus mejoras y envía un 'pull request'.

## Licencia
Este proyecto está bajo una licencia MIT. Consulta el archivo LICENSE para más detalles.
