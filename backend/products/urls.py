from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'product', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'cart-products', views.CartProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
 ]
