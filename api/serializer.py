from rest_framework import serializers

from storeapp.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'discount', 'old_price', 'category', 'slug', 'inventory', 'price']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categpry_id', 'title', 'slug']
