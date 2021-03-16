from django.urls import path
from . import views

urlpatterns = [
   path('', views.showForm, name='showForm'),
   path('post_review/', views.post_revieForm, name='postReviewForm')
]