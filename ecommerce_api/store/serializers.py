from rest_framework import serializers
from .models import Category, Product
from django.contrib.auth.models import User

# Serializer for the User model to handle user registration
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) #write only field for security can only send pass when creating cant recieve it when viewing

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CategorySerializer(serializers.ModelSerializer): #serializer for the Category model
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer): #serializer for the Product model
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'created_at', 'image', 'created_by', 'stock_quantity']
        read_only_fields = ['id', 'created_at', 'created_by'] #fields that should not be modified directly

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("price must be a positive number")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("stock quantity must be a positive number")
        return value
    
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cant be empty")
        return value
