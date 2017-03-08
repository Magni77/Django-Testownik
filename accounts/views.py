from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
    )
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import UserCreateSerializer,  UserDetailSerializer, PasswordSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'


       # else:
       #     return PasswordSerializer
    # def retrieve(self, request, username=None):
    #     context = {'request': request}
    #     instance = self.get_object()
    #    # serializer = self.get_serializer(instance)
    #
    #     obj = UserDetailSerializer(instance)
    #     serializer = self.get_serializer(instance)
    #
    #     return Response(serializer.data)
    # # def register(self, request, pk=None):
    # #     pass


    @detail_route(methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly], url_path='change-password')
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