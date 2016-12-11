from django.conf.urls import url, include

from rest_framework import routers
from .views import IndexView
from .viewSets import RestaurantViewSet#, CategoryViewSet, PaymentViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, base_name = "restaurants")
# router.register(r'categories', CategoryViewSet, base_name = "categories")
# router.register(r'payments', PaymentViewSet, base_name = "payments")
# router.register(r'cities', CityViewSet, base_name = "cities")

urlpatterns = [
    url(r'^$', IndexView.as_view()),

    url(r'^api/', include(router.urls)),
]