from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'', views.ProductViewSet)
router.register(r'catalog', views.CatalogViewSet)
router.register(r'cart', views.CartProductViewSet)
router.register(r'photos', views.PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
 ]
