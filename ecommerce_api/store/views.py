from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter


# my Shop views here.
class CategoryViewSet(viewsets.ModelViewSet): 
    queryset = Category.objects.all() #fetch all categories from the DB
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() #fetch all products from the DB
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [SearchFilter] #enable search functionality
    search_fields = ['name', 'description']
    filterset_fields = ['category'] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) #automatically set the created_by field to the current user when a product is created
