from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2) #used a decimal field since some prices have cents
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) #image field to upload product images
    created_by = models.ForeignKey(User, related_name='products', on_delete = models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=1) #quantity field to track number of items in cart


