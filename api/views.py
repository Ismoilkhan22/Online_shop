from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializer import ProductSerializer, CategorySerializer
from storeapp.models import Product, Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

"""
birnchi usul product crud 

"""
# @api_view(['GET'], ['POST'])
# def api_products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['GET'], ['PUT'], ['DELETE'])
# def api_product(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
"""
ikkinchi usul product crud 
class lar bilan 
"""


# class ApiProducts(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class ApiProduct(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, id=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         product = get_object_or_404(Product, id=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         product = get_object_or_404(Product, id=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class ApiProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ApiProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# @api_view(['GET'])
# def api_categories(request):
#     if request.method == 'GET':
#     categories = Category.objects.all()
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data)
#
# #
# @api_view(['GET'])
# def api_category(request, pk):
#     category = get_object_or_404(Category, category_id=pk)
#     serializer = CategorySerializer(category)
#     return Response(serializer.data)


# class ApiCategories(APIView):
#     """
#     bu kategoriyalar uchun crud qilishni 2- usuli edi barcha categoriyalarni chiqqarib beradi va post qushadi
#     """
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class ApiCategory(APIView):
"""
bu ham shunaqa ikkinchi usuli  update delete 
"""


#     def get(self, request, pk):
#         category = get_object_or_404(Category, category_id=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         category = get_object_or_404(Category, category_id=pk)
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         category = get_object_or_404(Category, category_id=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

class ApiCategories(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ApiCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
