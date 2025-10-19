from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, UserViewSet




#sets up a router for the API endpoints also gives us a browsable API
router = DefaultRouter() 
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
