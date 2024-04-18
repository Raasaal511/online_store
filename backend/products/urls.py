from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'productlist', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'cart', views.CartProductViewSet)
router.register(r'photos', views.PhotoViewSet)  # Надо проверить на правильность

urlpatterns = [
    path('', include(router.urls)),
 ]
