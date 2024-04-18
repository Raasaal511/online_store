from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('rest_framework.urls')),

    path(r'api/v1/auth/', include('djoser.urls')),
    path(r'api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/users/', include('users.urls')),
    path('api/v1/products/', include('products.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
