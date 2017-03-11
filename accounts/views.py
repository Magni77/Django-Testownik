from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
    )
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import UserCreateSerializer,  UserDetailSerializer, PasswordSerializer, UserBasicDetailsSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def post(self):
        pass

    @detail_route(methods=['POST'], permission_classes=[IsAuthenticatedOrReadOnly], url_path='change-password')
    def set_password(self, request, username=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=HTTP_400_BAD_REQUEST)

    @list_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request,  *args, **kwargs):
        """
        Returns authenticated user info
        """
        self.kwargs.update(username=request.user.username)
        user = self.get_object()
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLogOutAPIView(APIView):
    pass


# class UserDetailsAPIView(RetrieveUpdateAPIView):
#     serializer_class = UserDetailSerializer
#     queryset = User.objects.all()
#     lookup_field = 'username'
#    # permission_classes = [AllowAny]