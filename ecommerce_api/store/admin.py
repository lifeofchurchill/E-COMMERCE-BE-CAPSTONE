from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at', 'created_by', 'stock_quantity')
    list_filter = ('category', 'created_at', 'created_by')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

admin.site.register(Product, ProductAdmin)
