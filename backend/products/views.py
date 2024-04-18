import django_filters
from django.db.models import Sum, F
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product, Category, CartProduct, Photo
from .serializers import ProductSerializer, CategorySerializer, CartProductSerializer, PhotoSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


# Надо посмотреть что делать с veiw моделью Photo
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        cart_products = CartProduct.objects.all().filter(cart__owner=self.request.user.id)
        # Умножает сумму продукта на количество в карзине  и фильтрует его по пользователю
        cart_products = cart_products.annotate(
            total_product_price=Sum(F('product__price') * F('quantity')))

        # Получает всю сумму товаров от продуктов в корзине
        cart_total_price = cart_products.filter(ordering=True).aggregate(
            total_cost_cart=Sum('total_product_price'))

        serializer = CartProductSerializer(cart_products, many=True)

        return Response({
            'products': serializer.data,
            'total_cost_cart': cart_total_price['total_cost_cart'] if cart_total_price['total_cost_cart'] else 0
        }, status=status.HTTP_200_OK)
