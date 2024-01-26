from rest_framework import serializers

from .models import Product, Category, Photo, Cart, CartProduct


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'photos', 'category')

    def create(self, validated_data):
        category, created = Category.objects.get_or_create(name=validated_data['category'])

        product = Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            category=category,
        )

        Photo.objects.create(product=product, image=validated_data['photos']['image'])

        return product


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('owner',)


class CartProductSerializer(serializers.ModelSerializer):
    total_product_price = serializers.IntegerField(read_only=True)
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = ('product', 'cart', 'ordering', 'quantity', 'total_product_price')
