from rest_framework.viewsets import ModelViewSet

from api.serializer import ProductSerializer, CategorySerializer
from storeapp.models import Product, Category
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ApiProduct2(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backend = [DjangoFilterBackend,]
    filter_fields = ['category_id', 'old_price']
    # search_fields = ['name', 'description']
    # ordering_fields = ['old_price']


class ApiCategory2(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
