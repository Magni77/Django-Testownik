from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        ListField,
                                        FileField,
                                        ReadOnlyField)
from rest_framework import serializers

from comments.models import CommentModel
from comments.serializers import CommentDetailSerializer
from tests.models import TestModel, QuestionModel, AnswerModel
from tests.models import UploadFileModel, TestMarkModel


class UploadFileSerializer(ModelSerializer):
    files = ListField(
        child=FileField(max_length=100000,
                        allow_empty_file=False,
                        use_url=False)
    )

    class Meta:
        model = UploadFileModel
        fields = ['files',
                  'encoding',
                  'test_choice',
                  ]


class TestListSerializer(ModelSerializer):
    questions_count = SerializerMethodField()
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = TestModel
        fields = [
       #     'url',
            'id',
            'user',
            'title',
            'description',
            'questions_count',
            'is_public',
        ]

    def get_questions_count(self, obj):
        qs = QuestionModel.objects.filter(test=obj.id)
        return len(qs)


class AnswerSerializer(ModelSerializer):
   ##     view_name='tests-api:answerDetail')

    class Meta:
        model = AnswerModel

        fields = [
           # 'url',
            'id',
            'answer',
            'img_answer',
            'is_correct',
      #      'question'
        ]
        read_only = ['question']


class QuestionSerializer(ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionModel
        fields = [
        #    'url',
            'id',
            'question',
            'img_question',
            'hint',
            'test',
            'answers'

        ]


class QuestionDetailSerializer(ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = [
            'id',
            'question',
            'img_question',
            'hint',
        ]


class TestSerializer(ModelSerializer):
    questions_count = SerializerMethodField()
    comments = SerializerMethodField()
    questions = QuestionSerializer(many=True, read_only=True)
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = TestModel
        fields = [
            'id',
            'user',
            'title',
            'description',
            'questions_count',
            'mark',
            'is_public',
            'comments',
            'questions',

        ]

    def get_questions(self, obj):
        qs = QuestionModel.objects.filter(test=obj.id) #filter(content_type = obj.__class__)
        questions = QuestionSerializer(qs, many=True).data
        return questions

    def get_questions_count(self, obj):
        qs = QuestionModel.objects.filter(test=obj.id)
        return len(qs)

    def get_comments(self, obj):
        qs = CommentModel.objects.filter(object_id=obj.id)
        return CommentDetailSerializer(qs, many=True).data


class MarkSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = TestMarkModel
        fields = ['user', 'mark']

