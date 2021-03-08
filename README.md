# Django_Web_Demo

Esta es una aplicación web desarrollada con Django para exponer a nuestros compañeros de clase cómo trabajar con este framework.

### Requisitos 📋

Para empezar con este proyecto es necesario tener instalado Python y pip


Para instalar Python descargar el ejecutable y seguir los pasos
```
https://www.python.org/downloads/
```

Adicionalmente instalar pip, que es el gestor de paquetes de Python ejecutando el siguiente comando
```
py get-pip.py
```
## Creación del entorno virtual 📦

En primer lugar instalar el gestor de entornos mediante el administrador de paquetes
```
pip install virtualenv
```
Para crear el entorno virtual
```
virtualenv web_env
```
Esto creará el directorio web_env, el cual tiene la siguiente estructura
```
/web_env
   |__ /Lib
   |__ /Scripts
   |__ .gitignore
   |__ pyenv.cfg
```
El directorio /Lib contiene las librerías necesarias para correr nuestro código.
El directorio /Scripts contiene los ejecutables: como el intérprete de Python o pip.

Para listar todos los paquetes y/o librerías instalados en el entorno virtual 
```
pip freeze
pip list
```
Para activar y desactivar el entorno ingresamos al directorio del entorno cd .\web_env\ y una vez dentro del directorio \web_env se puede activar o desactivar el entorno con los siguientes comandos
```
.\Scripts\activate
deactivate
```

### Instalación 🔧

Para instalar Django ejecutar dentro del entorno virtual \web_env
```
pip install django
```
Podemos tambien comprobar la version del framework con el comando
```
django-admin --version
```
Una vez instalado el framework con sus dependencias en el entorno virtual podemos crear el proyecto
```
django-admin startproject webDemo
```
Esto creará un directorio .\webDemo dentro del entorno virtual con la siguiente estructura
```
webDemo/
    |__ manage.py
    |__ webDemo/
        |__ __init__.py
        |__ asgi.py
        |__ settings.py
        |__ urls.py
        |__ wsgi.py
```

