from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD

# Create your views here.
def index(request):
   return HttpResponse("Hello, World!")
# Create your views here.
=======
from .models import Order,Client
 
# Create your views here.
def index(request):
    orders = Order.objects.all()
    context = {
        'titulo_pagina': 'Ordenes del Restaurante',
        'listado_ordenes': orders
    }
    return render(request, 'orders.html' ,context)

def cliente_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    context = {
        'titulo_pagina': 'Detalles del Cliente',
        'cliente': client
    }
    return render(request, 'client.html' ,context)
    
>>>>>>> ccee2712926624bdd6ec1ca35fedfc75786802af
