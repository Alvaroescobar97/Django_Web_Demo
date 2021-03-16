from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponse

# Create your views here.
def showForm(request):
    form = ReviewForm()
    return render(request, 'review.html',{'form':form})
    
def post_revieForm(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        nombre_restaurante = form.cleaned_data['name_restaurant']
        nombre_cliente = form.cleaned_data['name_client']
        resenia = form.cleaned_data['review']
        direccion = form.cleaned_data['address']
        calificacion = form.cleaned_data['stars']
        return HttpResponse(f"Restaurante: {nombre_restaurante} - Cliente: {nombre_cliente} - Reseña: {resenia} - Direccion Restaurante: {direccion} - Calificación: {calificacion}")