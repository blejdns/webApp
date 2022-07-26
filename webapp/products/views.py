from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import ProductSerializer
from .models import Product


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer