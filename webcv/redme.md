# README del Proyecto de Ecommerce Comunitario
Este es un proyecto de ecommerce comunitario desarrollado con el framework Django. En este archivo README se proporciona información detallada sobre cómo crear y configurar el entorno de trabajo, las carpetas utilizadas en el proyecto, cómo iniciar el servidor, crear tablas y modelos, y consultar la base de datos.

## Creación de Entorno de Trabajo y Entorno Virtual
Para crear el entorno de trabajo y el entorno virtual, se deben seguir los siguientes pasos:

### 1. Verificar la versión de Python en la terminal:
`python3 —version`

### 2. Ingresar a la carpeta webcv, navegar a ella:

`
cd comuniveta
cd webcv
`
###3. Si tu computador es mac os:

#### Crear un entorno virtual utilizando el comando venv:

`python3 -m venv venv`

#### Activar el entorno virtual:

`source venv/bin/activate`

#### pip install django

`pip install django`

#### instalar django (use preferencialmente este comando)
https://docs.djangoproject.com/en/4.2/topics/install/

`python -m pip install Django`

## Carpetas

Este proyecto consta de una carpeta de proyecto llamada "project1", donde Django no afecta la carpeta, y una carpeta interna también llamada "project1", que sí está afectada por Django.

### Servidor

Para iniciar el servidor, se debe ejecutar el siguiente comando en la terminal:

`python3 manage.py runserver`

## Crear Tablas
- Para crear tablas, se deben seguir los siguientes pasos:

#### Ejecutar el siguiente comando en la terminal:

`python3 manage.py migrate`

`python3 manage.py createsuperuser`


