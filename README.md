# CECyTE-web

Instrucciones para correr proyecto por primera vez

## Instalar paquetes necesarios

```bash
pip install -r requirements.txt 
```


## Configurar base de datos

Crear una base de datos que se llame ***cecyte***

```bash
python manage.py makemigrations
python manage.py migrate
```
Ejecutar en la base de datos el script primer_insert.sql

## Ejecutar el proyecto

Presionar F5 en Visual Studio Code o en terminal

```bash
python manage.py runserver 0.0.0.0:8000
```

En el navegador estará corriendo en http://localhost:8000/
