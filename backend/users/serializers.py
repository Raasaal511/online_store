from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = PasswordField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_mobile=validated_data.get('phone_mobile', None)
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
