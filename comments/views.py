from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
    )
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from rest_framework.response import Response

from .models import CommentModel
from .serializers import CommentDetailSerializer, CommentCreateSerializer
from tests.models import TestModel, QuestionModel
from django.contrib.contenttypes.models import ContentType


class CreateCommentAPIView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentDetailSerializer


class TestListAPIView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentDetailSerializer


def get_model_type(data):
    if data == 'test':
        return TestModel
    elif data == 'question':
        return QuestionModel


class TestCommentCreateAPIView(ListCreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentDetailSerializer

    def list(self, request, *args, **kwargs):
        ct = ContentType.objects.get_for_model(get_model_type(kwargs['type']))
        queryset = CommentModel.objects.filter(object_id=kwargs['pk'], content_type=ct)

        return Response(CommentDetailSerializer(queryset, many=True).data)

    def create(self, request, *args, **kwargs):
        serializer = CommentDetailSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            ct = ContentType.objects.get_for_model(get_model_type(kwargs['type']))
            obj = CommentModel(
                user=request.user,
                content=data['content'],
                content_type=ct,
                object_id=kwargs['pk']
            )
            obj.save()
            return Response({'status': 'created'}, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
