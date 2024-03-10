from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.serializer import ProductSerializer, CategorySerializer, ReviewSerializer, CartSerializer
from storeapp.models import Product, Category, Review, Cart
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin

class ApiProduct2(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['category_id', 'old_price']
    # search_fields = ['name', 'description']
    # ordering_fields = ['old_price']
    pagination_class = PageNumberPagination


class ApiCategory2(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CartViewSet(CreateModelMixin, GenericViewSet):
    queryset = Cart.object.all()
    serializer_class = CartSerializer
