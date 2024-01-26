from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class ProfileAPIView(APIView):
    def get(self, request):
        profile = Profile.objects.get(user_id=request.user.id)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
