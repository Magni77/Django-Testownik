from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from .models import LearningSession
from .serializers import LearningSessionListSerializer, LearningSessionSerializer, LearningSessionCreateSerializer

User = get_user_model()


class LearningSessionViewSet(viewsets.ModelViewSet):
 #   serializer_class = LearningSessionSerializer
    queryset = LearningSession.objects.all()

    def get_serializer_class(self):
        if self.action in ('list'):
            return LearningSessionListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return LearningSessionCreateSerializer
        else:
            return LearningSessionSerializer

    def get_queryset(self):
        user = self.request.user
        return user.learningsession_set.all()

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #    # print(self.get_object())
    #    # serializer = QuestionStatisticSerializer
    #     print(data)
    #     return Response({'status': 'password set'})


class LearingSessionCreateAPIView(CreateAPIView):
    queryset = LearningSession.objects.all()
    serializer_class = LearningSessionCreateSerializer