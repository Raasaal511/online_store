from rest_framework import serializers

from .models import Product, Category, Photo, Cart, CartProduct


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category_name']

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('product.name', 'image')


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('cart', 'product', 'ordering')
