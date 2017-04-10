from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LearningSession, QuestionStatistic
from .serializers import (LearningSessionListSerializer,
                          LearningSessionSerializer,
                          LearningSessionCreateSerializer,
                          QuestionStatisticSerializer,
                          QuestionStatisticDetailSerializer)

User = get_user_model()


class LearningSessionListAPIView(generics.ListCreateAPIView):
    serializer_class = LearningSessionCreateSerializer

    def get_queryset(self):
        return LearningSession.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        qs = LearningSession.objects.filter(user=self.request.user)
        for session in qs:
            session.is_active = False
            session.save()

        serializer.save(
            user=self.request.user,
            is_active=True
        )


class LearningSessionDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LearningSessionSerializer

    def get_queryset(self):
        return LearningSession.objects.filter(
            user=self.request.user
        )


class StatisticsListAPIView(generics.ListAPIView):
    serializer_class = QuestionStatisticSerializer

    def get_queryset(self):
        return QuestionStatistic.objects.filter(
            learning_session=self.kwargs.get('pk'))


class StatisticsDetailAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionStatisticDetailSerializer

    def get_queryset(self):
        return QuestionStatistic.objects.filter(
            learning_session=self.kwargs.get('pk'))

    def get_object(self):
        qs = self.get_queryset()
        return get_object_or_404(qs, id=self.kwargs.get('pk_question'))


class StatisticsAnswerAPIView(APIView):
    """GET:  Add correct/wrong answer statistics
    /correct/ => correct_answers += 1
    /wrong/ => wrong_answers += 1
    If objects replies <= 0 only return data
    """

    def get(self, request, pk=None, pk_question=None, answer=None):
        obj = get_object_or_404(QuestionStatistic,
                                learning_session=pk,
                                id=pk_question
                                )
        if obj.replies > 0:
            if answer == 'correct':
                obj.correct_answers += 1
                obj.replies -= 1
            else:
                obj.wrong_answers += 1
                obj.replies += 1
            obj.save()

        return Response({'correct_answers': obj.correct_answers,
                         'wrong_answers': obj.wrong_answers,
                         'replies': obj.replies
                         })

