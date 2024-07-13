import django_filters
from django.db.models import Sum, F
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product, Catalog, CartProduct, Photo
from .serializers import ProductSerializer, CatalogSerializer, CartProductSerializer, PhotoSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
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
        cart_products = self.get_filtered_cart_products(user_id=self.request.user.id)
        cart_total_price = self.get_cart_total_price(cart_products)

        serializer = CartProductSerializer(cart_products, many=True)

        return Response({
            'products': serializer.data,
            'total_cost_cart': cart_total_price if cart_total_price else 0
        }, status=status.HTTP_200_OK)

    def get_filtered_cart_products(self, user_id):
        """Умножает сумму продукта на количество в карзине для пользователя."""
        cart_products = CartProduct.objects.filter(cart__owner=user_id)
        return cart_products.annotate(
            total_product_price=Sum(F('product__price') * F('quantity'))
        )

    def get_cart_total_price(self, cart_products):
        """Получает всю сумму товаров от продуктов в корзине который находитсья в заказе."""
        total_price = cart_products.filter(ordering=True).aggregate(
            total_cost_cart=Sum('total_product_price'))
        return total_price['total_cost_cart']
