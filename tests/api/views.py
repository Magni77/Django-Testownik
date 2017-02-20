from rest_framework.generics import ListAPIView, RetrieveAPIView

from tests.models import TestModel, QuestionModel
from .serializers import TestSerializer, QuestionSerializer


class TestListAPIView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionListAPIView(ListAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class TestDetailAPIView(RetrieveAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer