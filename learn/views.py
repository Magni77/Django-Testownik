from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .models import LearningSession, QuestionStatistic
from .serializers import (LearningSessionListSerializer,
                          LearningSessionSerializer,
                          LearningSessionCreateSerializer,
                          QuestionStatisticSerializer)

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

    @detail_route()
    def statistics(self, request, pk=None):
        qs = QuestionStatistic.objects.filter(learning_session=pk)
        serializer = QuestionStatisticSerializer(qs, many=True)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #    # print(self.get_object())
    #    # serializer = QuestionStatisticSerializer
    #     print(data)
    #     return Response({'status': 'password set'})

