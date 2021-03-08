# 🚀 Django_Web_Demo

Esta es una aplicación web desarrollada con Django para exponer a nuestros compañeros de clase cómo trabajar con este framework.

### 📋 Requisitos 

Para empezar con este proyecto es necesario tener instalado Python y pip


Para instalar Python descargar el ejecutable y seguir los pasos
```
https://www.python.org/downloads/
```

Adicionalmente instalar pip, que es el gestor de paquetes de Python ejecutando el siguiente comando
```
py get-pip.py
```
## 📦 Creación del entorno virtual 

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

### 🛠️ Instalación 

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
El directorio exterior ```webDemo/``` es la carpeta del proyecto.

```manage.py``` es una utilidad para la linea de comandos (CLI) que permite interactuar con el proyecto de Django de varias formas. Para más información: https://docs.djangoproject.com/en/1.8/ref/django-admin/

El directorio interno ```webDemo/``` es el paquete de Python real para su proyecto. Su nombre es el nombre del paquete de Python que necesitará usar para importar cualquier cosa dentro de él (Ej: webDemo.urls).

```__ init__.py``` es un archivo vacío que le dice a Python que este directorio debe considerarse un paquete de Python.

```settings.py```  configuración para este proyecto de Django. Para más información: https://docs.djangoproject.com/en/1.8/topics/settings/

```urls.py``` son las declaraciones de las URL’s para este proyecto de Django. Puntos de entrada para la aplicación.

```wsgi.py``` es un punto de entrada para servidores web compatibles con WSGI para servir su proyecto.

```asgi.py``` además de WSGI, Django también admite la implementación en ASGI, el estándar emergente de Python para aplicaciones y servidores web asíncronos.

Formas de interactuar con el framework
```
$ django-admin <command> [options]
$ python manage.py <command> [options]
```

### 🔩 Arquitectura y Estructura 

Para comprobar que el proyecto funciona dentro del directorio del proyecto ```webDemo\``` ejecutamos el siguiente comando para iniciar el servidor local de nuestro proyecto.
```
python manage.py runserver
```
Deberiamos ver la siguiente linea en la consola ```Starting development server at http://127.0.0.1:8000/```

Django viene con una utilidad que genera automáticamente la estructura de directorios básica para una aplicación, por lo que podemos concentrarnos en escribir código en lugar de crear directorios.

_Nota:    Proyectos vs. Aplicaciones_
Una aplicación es una aplicación web que hace algo, por ejemplo, un sistema de registro web, una base de datos de registros públicos o una aplicación de encuesta simple. Un proyecto es una colección de configuraciones y aplicaciones para un sitio web en particular. Un proyecto puede contener varias aplicaciones. Una aplicación puede estar en varios proyectos.

Para crear una aplicación, hay que asegurarse de estar en el directorio exterior ```webDemo/``` pa interactuar con ```manage.py``` y ejecutar el siguiente comando
```
python manage.py startapp restaurant
```

Eso creará un directorio ```\restaurant```, que tiene la siguiente estructura

```
restaurant/
    |__ migrations/
        |__ _init_.py
    |__ __init__.py
    |__ admin.py
    |__ apps.py
    |__models.py
    |__tests.py
    |__views.py
```
Una vez creada la aplicación se debe agregar a la lista de aplicaciones instaladas en el archivo ```webDemo/settings.py``` de la siguiente manera
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',
)
```
### ⌨️ Primeros pasos 

Para empezar vamos a crear la primera vista con Django en el archivo ```views.py``` dentro del directorio de la aplicación restaurant


### ✒️ Autores 

* Álvaro José Escobar González
* Juan Manuel Castillo Herrera

