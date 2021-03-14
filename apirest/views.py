from django.views import View
from .models import Restaurant
from django.http import JsonResponse
from django.forms.models import model_to_dict


class RestaurantListView(View):
    def get(self, request):
        if('name' in request.GET):
            restaurantList = Restaurant.objects.filter(name__contains=request.GET['name'])
        else:     
            restaurantList = Restaurant.objects.all()
        return JsonResponse(list(restaurantList.values()), safe=False)


class RestaurantDetailView(View):
    def get(self, request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        return JsonResponse(model_to_dict(restaurant))
