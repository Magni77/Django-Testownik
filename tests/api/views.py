from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveUpdateDestroyAPIView
    )

from tests.models import TestModel, QuestionModel, AnswerModel
from .serializers import TestSerializer, TestListSerializer, QuestionSerializer, AnswerSerializer


class TestListAPIView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestListSerializer


class QuestionListAPIView(ListAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


#details
class TestDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer


#create views
class TestCreateAPIView(CreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    #authentication_classes = TokenAuthentication


class QuestionCreateAPIView(CreateAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateAPIView(CreateAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer
