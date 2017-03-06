from .serializers import LearningSessionSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from .models import LearningSession
User = get_user_model()


class LearningSessionAPIView(RetrieveUpdateAPIView):
    serializer_class = LearningSessionSerializer
    queryset = LearningSession.objects.all()


class LearningSessionListAPIView(ListAPIView):
    serializer_class = LearningSessionSerializer
    queryset = LearningSession.objects.all()