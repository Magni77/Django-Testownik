from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    DestroyAPIView, RetrieveUpdateAPIView
    )

from tests.models import TestModel, QuestionModel, AnswerModel
from .serializers import TestSerializer, QuestionSerializer, AnswerSerializer


class TestListAPIView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionListAPIView(ListAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


#details
class TestDetailAPIView(RetrieveAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionDetailAPIView(RetrieveAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerDetailAPIView(RetrieveAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

#create views
class TestCreateAPIView(CreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionCreateAPIView(CreateAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateAPIView(CreateAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer


#edit
class TestEditAPIView(RetrieveUpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionEditAPIView(RetrieveUpdateAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerEditAPIView(RetrieveUpdateAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer


#delete
class TestDeleteAPIView(DestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionDeleteAPIView(DestroyAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerDeleteAPIView(DestroyAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer
