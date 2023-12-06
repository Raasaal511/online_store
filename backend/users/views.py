from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UserSerializer, UserRegisterSerializer, ProfileSerializer


class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = {
            'username': serializer.data['username'],
            'email': serializer.data['email'],
        }
        return Response(user_data, status=status.HTTP_201_CREATED)


class ProfileAPIView(APIView):
    def get(self, request):
        profile = Profile.objects.get(user_id=request.user.id)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
