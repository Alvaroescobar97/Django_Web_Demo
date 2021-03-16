from django import forms

class ReviewForm(forms.Form):
    name_restaurant = forms.CharField(label="Nombre Restaurante ", max_length=100)
    name_client = forms.CharField(label="Nombre Cliente ", max_length=150)
    review = forms.CharField(label="Reseña ", max_length=250)
    address = forms.CharField(label="Direccion del Restaurante")
    stars = forms.IntegerField(label="Calificación ")