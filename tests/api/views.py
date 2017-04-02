from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    )
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from tests.models import TestModel, QuestionModel, AnswerModel, TestMarkModel
from tests.models import UploadFileModel
from tests.upload_handler import UploadHandler
from .serializers import TestSerializer, TestListSerializer, \
    QuestionSerializer, AnswerSerializer, UploadFileSerializer, MarkSerializer


class TestListAPIView(ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestListSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )


#details
class TestDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


#create views
class TestCreateAPIView(CreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )


class QuestionCreateAPIView(CreateAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateAPIView(CreateAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer


class TestUploadView(CreateAPIView):
    queryset = UploadFileModel
    serializer_class = UploadFileSerializer

    def create(self, request, filename=None, format=None):
        files = request.FILES.getlist('file')

        UploadHandler(request, files, request, is_rest=True)
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)


class TestMarkAPIView(ListCreateAPIView):
    queryset = TestMarkModel.objects.all()
    serializer_class = MarkSerializer

    def list(self, request, *args, **kwargs):
        queryset = TestMarkModel.objects.filter(test=kwargs['pk'])
        qs = [x.mark for x in queryset]
        if len(qs) > 0:
            return Response({'mark': sum(qs) / len(qs)})
        return Response({'mark': 0})

    def create(self, request, *args, **kwargs):
        serializer = MarkSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            test = TestModel.objects.filter(id=kwargs['pk'])
            obj = TestMarkModel(
                user=request.user,
                test=test.first(),
                mark=data['mark']
            )
            obj.save()
            return Response({'status': 'created'})
        else:
            return Response(serializer.errors)


class QuestionListAPIView(ListCreateAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return QuestionModel.objects.filter(test=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        test_obj = get_object_or_404(TestModel, id=self.kwargs.get('pk'))
        serializer.save(
            user=self.request.user,
            test=test_obj
        )


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return QuestionModel.objects.filter(test=self.kwargs.get('pk'))

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), id=self.kwargs.get('question_id'))
        return obj


class AnswersListAPIView(ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return AnswerModel.objects.filter(question=self.kwargs.get('question_id'))

    def perform_create(self, serializer):
        question_obj = get_object_or_404(QuestionModel, id=self.kwargs.get('question_id'))
        serializer.save(
            user=self.request.user,
            question=question_obj
        )


class AnswerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    queryset = AnswerModel

    def get_queryset(self):
        return AnswerModel.objects.filter(question=self.kwargs.get('question_id'))

    def get_object(self):
        qs = self.get_queryset()
        obj = get_object_or_404(qs, id=self.kwargs.get('answer_id'))
        return obj
