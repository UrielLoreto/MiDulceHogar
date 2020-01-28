from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView,
    CreateAPIView
    )
from rest_framework .filters import SearchFilter, OrderingFilter
from .models import Product, Sale
from .serializers import (
    ProductSerializer, 
    ProductPriceSerializer, 
    ProductDescriptionSerializer, 
    SaleSerializer,
    SaleCreateSerializer,
    ProductCreateSerializer
    )

class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProducDeletetView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProducUpdatePriceView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductPriceSerializer
    lookup_field = 'id'

class ProducUpdateDescriptionView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDescriptionSerializer
    lookup_field = 'id'

class ProductGeyByName(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description', 'sku')

class ProductGeyById(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class SaleCreateView(CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleCreateSerializer

class SaleView(ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer