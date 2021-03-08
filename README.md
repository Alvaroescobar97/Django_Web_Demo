# 🚀 Django_Web_Demo

Esta es una aplicación web desarrollada con Django y explicada para que cualquiera que quiera aprender a desarrollar aplicaciones web con Python & Django pueda seguir esta guia y aprender a trabajar con este maravilloso framework.

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
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return HttpResponse("Hello World!")
```
Ahora bien, para poder acceder a esta vista desde el navegador se debe configurar la ruta de entrada a esa vista en un nuevo archivo de Python que se crea de la siguiente manera: Damos click derecho sobre la carpeta de la aplicación ```\restaurant``` , New -> Python File, especificamos el nombre ```urls.py``` y declaramos las variables así: 
```
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index')
]
```
Y por último, debemos enlazar el archivo ```restaurant\urls.py``` de la aplicación con el archivo ```webDemo\urls.py``` del proyecto.
```
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('webDemo/', include('restaurant.urls'))
]
```
Si entramos a la ruta http://127.0.0.1:8000/webDemo/ desde el navegador podemos ver nuestro primer "Hello World!" en Django :)

Luego de crear nuestra primera vista debemos definir el modelo de nuestra aplicación dentro del archivo ```restaurant\models.py```
```
from django.db import models

# Create your models here.

class Ingrediente(models.Model):
   nombre = models.CharField(max_length=50)
   cantidad = models.IntegerField(default=0)

   def __str__(self):
       return f"id={self.id}, nombre={self.nombre},cantidad={self.cantidad}"

class Plato(models.Model):
   nombre = models.CharField(max_length=50)
   descripcion = models.CharField(max_length=50)
   ingredientes = models.ManyToManyField(Ingrediente)

   def __str__(self):
       return f"id={self.id}, nombre={self.nombre},descripcion={self.descripcion},ingredientes={self.ingredientes}"
```
Una vez tenemos definido el modelo se puede ejecutar el siguiente comando para crear las migraciones que se plasmarán en el modelo en la base de datos
```
python manage.py makemigrations restaurant
```
Habiendo creado las migraciones se puede proceder a migrar el modelo que definimos a la base de datos mediante el siguiente comando
```
python manage.py migrate
```
Lo que creará un nuevo archivo en la carpeta ```restaurant\migrations``` con el historial de las migraciones realizadas.

Si quisieramos obtener más información o cambiar la base de datos del proyecto (SQLite) podemos configurar esto en el archivo ```settings.py``` del proyecto.
```
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


### ✒️ Autores 

* Álvaro José Escobar González
* Juan Manuel Castillo Herrera

