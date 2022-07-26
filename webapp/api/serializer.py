from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Car


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.CharField(
        source="author.username", read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'type', 'power', 'weight', 'author']


class CarSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'type', 'power', 'weight', 'author']