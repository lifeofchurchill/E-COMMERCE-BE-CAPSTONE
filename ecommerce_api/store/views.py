from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer, UserSerializer
from .models import Category, Product
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User


# my Shop views here.
class CategoryViewSet(viewsets.ModelViewSet): 
    queryset = Category.objects.all() #fetch all categories from the DB
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() #fetch all products from the DB
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [DjangoFilterBackend, SearchFilter] #enable filtering and searching
    search_fields = ['name', 'description']
    filterset_fields = ['category', 'price', 'stock_quantity'] 
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) #automatically set the created_by field to the current user when a product is created

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
