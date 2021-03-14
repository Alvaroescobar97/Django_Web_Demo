from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('cliente/<int:client_id>', views.cliente_detail, name='cliente')
]

