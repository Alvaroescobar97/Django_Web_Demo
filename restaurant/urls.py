from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
   path('', views.index, name='index')
]
=======
   path('', views.index, name='index'),
   path('cliente/<int:client_id>', views.cliente_detail, name='cliente')
]
>>>>>>> ccee2712926624bdd6ec1ca35fedfc75786802af
