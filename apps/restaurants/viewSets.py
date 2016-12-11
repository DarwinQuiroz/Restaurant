from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
	model = Restaurant
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer