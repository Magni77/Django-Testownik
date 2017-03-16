from rest_framework.serializers import (ModelSerializer,
                                        Serializer,
                                        SerializerMethodField,
                                        ListField,
                                        FileField,
                                        ValidationError)
from tests.models import TestModel, QuestionModel, AnswerModel
from tests.models import UploadFileModel
from comments.models import CommentModel
from comments.serializers import CommentDetailSerializer
from django.conf import settings


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
  #  url = HyperlinkedIdentityField(
  #       view_name='tests-api:testDetail')
   # user = UserBasicDetailsSerializer()
    questions_count = SerializerMethodField()

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
    #
    # def get_user(self, obj):
    #     return str(obj.user.username)

    def get_questions_count(self, obj):
        qs = QuestionModel.objects.filter(test=obj.id)
        return len(qs)


class TestSerializer(ModelSerializer):
    questions = SerializerMethodField()
    questions_count = SerializerMethodField()
    comments = SerializerMethodField()
    #user = SerializerMethodField()

    class Meta:
        model = TestModel
        fields = [
            'id',
            'user',
            'title',
            'description',
            'questions_count',
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

    #def get_user(self, obj):
    #    return str(obj.user.username)


class QuestionSerializer(ModelSerializer):
    answers = SerializerMethodField()

   # url = HyperlinkedIdentityField(
   #     view_name='tests-api:questionDetail')

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

    def get_answers(self, obj):
        qs = AnswerModel.objects.filter(question=obj.id) #filter(content_type = obj.__class__)
        answers = AnswerSerializer(qs, many=True).data
        return answers


class AnswerSerializer(ModelSerializer):
   ##     view_name='tests-api:answerDetail')

    class Meta:
        model = AnswerModel

        fields = [
           # 'url',
            'id',
            'answer',
            'img_answer',
            'is_correct'

        ]
