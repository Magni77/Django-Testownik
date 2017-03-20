from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    )
from rest_framework.mixins import CreateModelMixin

from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from tests.models import TestModel, QuestionModel, AnswerModel, TestMarkModel
from .serializers import TestSerializer, TestListSerializer, QuestionSerializer, AnswerSerializer, UploadFileSerializer, MarkSerializer
from rest_framework.response import Response
from tests.models import UploadFileModel
from tests.upload_handler import UploadHandler
from rest_framework.permissions import AllowAny


class TestListAPIView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestListSerializer
    permission_classes = [AllowAny]


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
        sum = 0
        for x in queryset:
            sum += x.mark
        return Response({'average': sum / queryset.count()})

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
            return Response({'status': 'created'})#, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors) #,
                            #status=HTTP_400_BAD_REQUEST)