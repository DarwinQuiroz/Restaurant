from django.contrib import admin
from .models import Category, City, Tip, Restaurant, Payment, Stablishment

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)

@admin.register(City)
class AdminCity(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)

@admin.register(Tip)
class AdminTip(admin.ModelAdmin):
	list_display = ('restaurant', 'user', 'conten',)
	list_filter = ('restaurant', 'user',)

@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
	list_display = ('name', 'description',)
	list_filter = ('payment', 'category', 'name',)

admin.site.register(Payment)
class AdminPayment(admin.ModelAdmin):
	list_display = ('pay',)
	list_filter = ('pay',)

admin.site.register(Stablishment)
class AdminStablishment(admin.ModelAdmin):
	list_display = ('restaurant', 'city', 'addres',)
	list_filter = ('restaurant', 'city',)