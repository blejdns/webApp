from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Car
from .serializer import UserSerializer, CarSerializer, CarSerializer2


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarView(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]  # added
    filterset_fields = ['id', 'brand', 'model']  # added


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def car_list(request):
    try:
        id = request.query_params['id']
        cars = Car.objects.get(pk=id)
        serializer = CarSerializer2(cars)
    except:
        cars = Car.objects.all()
        serializer = CarSerializer2(cars, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
