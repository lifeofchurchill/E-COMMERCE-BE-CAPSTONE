from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer): #serializer for the Category model
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer): #serializer for the Product model
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'created_at', 'image', 'created_by', 'stock_quantity']
        read_only_fields = ['id', 'created_at', 'created_by'] #fields that should not be modified directly
