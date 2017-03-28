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
from .serializers import TestSerializer, TestListSerializer, QuestionSerializer, AnswerSerializer, UploadFileSerializer, MarkSerializer


class TestListAPIView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestListSerializer
    permission_classes = [AllowAny]


# class QuestionListAPIView(ListAPIView):
#     queryset = QuestionModel.objects.all()
#     serializer_class = QuestionSerializer


#details
class TestDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


# class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = QuestionModel.objects.all()
#     serializer_class = QuestionSerializer


# class AnswerDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = AnswerModel.objects.all()
#     serializer_class = AnswerSerializer


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
            return Response({'status': 'created'})#, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors) #,
                            #status=HTTP_400_BAD_REQUEST)


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        print(self.kwargs.get('pk'))
        return QuestionModel.objects.filter(test=self.kwargs.get('pk'))


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return QuestionModel.objects.filter(id=self.kwargs.get('question_id'))


class AnswersListAPIView(ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return AnswerModel.objects.filter(question=self.kwargs.get('question_id'))


class AnswerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return AnswerModel.objects.filter(id=self.kwargs.get('answer_id'))