from rest_framework.viewsets import ModelViewSet

from api.serializer import ProductSerializer, CategorySerializer
from storeapp.models import Product, Category


class ApiProduct2(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ApiCategory2(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer















