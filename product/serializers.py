from rest_framework import serializers
from product.models import Brand, Product, Category


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','ratings','price','brand','category']