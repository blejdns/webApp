from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CarView, car_list


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users/?', UserViewSet)
router.register(r'cars/?', CarView, basename='Cars')

urlpatterns = [
    path('car_list', car_list, name='car_list'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]