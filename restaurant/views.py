from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
 
# Create your views here.
def index(request):
    orders = Order.objects.all()
    context = {
        'titulo_pagina': 'Ordenes del Restaurante',
        'listado_ordenes': orders
    }
    return render(request, 'orders.html' ,context)