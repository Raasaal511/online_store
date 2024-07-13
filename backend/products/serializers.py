from rest_framework import serializers

from .models import Product, Catalog, Photo, Cart, CartProduct


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('product', 'image')


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Catalog.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'photos', 'category')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('owner',)


class CartProductSerializer(serializers.ModelSerializer):
    total_product_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = CartProduct
        fields = ('product', 'cart', 'ordering', 'quantity', 'total_product_price')
