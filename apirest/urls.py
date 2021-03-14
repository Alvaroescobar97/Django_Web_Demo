from django.urls import path
from .views import RestaurantListView
from .views import RestaurantDetailView

urlpatterns = [
    path('restaurant/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant')
]
