from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin): #admin config for Category model
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin) #add Category model to admin site with the above config


class ProductAdmin(admin.ModelAdmin): #admin config for Product model
    list_display = ('name', 'price', 'category', 'created_at', 'created_by', 'stock_quantity')
    list_filter = ('category', 'created_at', 'created_by')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

admin.site.register(Product, ProductAdmin) #add Product model to admin site with the above config
