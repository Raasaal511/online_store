from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserAPIView.as_view(), name='user-list'),
    path('profile/', views.ProfileAPIView.as_view(), name='profile'),
]