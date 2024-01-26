from django.db.models import Sum, F
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product, Category, CartProduct
from .serializers import ProductSerializer, CategorySerializer, CartProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        # Умножает сумму продукта на количество в карзине  и фильтрует его по пользователю
        cart_products = CartProduct.objects.annotate(
            total_product_price=Sum(F('product__price') * F('quantity')),
        ).filter(cart__owner=self.request.user.id)

        # Получает всю сумму товаров от продуктов в корзине
        cart_total_price = cart_products.filter(ordering=True).aggregate(
            total_cost_cart=Sum('total_product_price'))

        serializer = CartProductSerializer(cart_products, many=True)

        return Response({
            'products': serializer.data,
            'cart_total': cart_total_price
            }, status=status.HTTP_200_OK)
