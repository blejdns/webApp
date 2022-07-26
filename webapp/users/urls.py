from django.urls import path, include
from rest_framework import routers
from .views import UsersViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'all/?', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]