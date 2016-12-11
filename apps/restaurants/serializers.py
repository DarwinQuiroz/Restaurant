from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
	tips = serializers.SerializerMethodField()

	def get_tips(self, restaurant):
		tips = restaurant.tip_set.all().count()
		return tips

	class Meta:
		model = Restaurant
		exclude = ['payment', 'category']