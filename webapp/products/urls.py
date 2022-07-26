from django.urls import path, include
from rest_framework import routers
from .views import ProductsViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'all/?', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]