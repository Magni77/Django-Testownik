from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField

from tests.models import TestModel, QuestionModel, AnswerModel
#from learn.serializers import QuestionStatisticSerializer
#from learn.models import QuestionStatistic


class TestListSerializer(ModelSerializer):
   # url = HyperlinkedIdentityField(
    #     view_name='tests-api:testDetail')
   # user = UserBasicDetailsSerializer()
    questions_count = SerializerMethodField()

    class Meta:
        model = TestModel
        fields = [
         #   'url',
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
            'questions',

        ]

    def get_questions(self, obj):
        qs = QuestionModel.objects.filter(test=obj.id) #filter(content_type = obj.__class__)
        questions = QuestionSerializer(qs, many=True).data
        return questions

    def get_questions_count(self, obj):
        qs = QuestionModel.objects.filter(test=obj.id)
        return len(qs)

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


# class TestLearningSerializer(ModelSerializer):
#     questions = SerializerMethodField()
#     #user = SerializerMethodField()
#
#     class Meta:
#         model = TestModel
#         fields = [
#             'id',
#             'user',
#             'title',
#             'description',
#             'questions_count',
#             'is_public',
#             'questions',
#
#         ]
#
#     def get_questions(self, obj):
#         qs = QuestionModel.objects.filter(test=obj.id) #filter(content_type = obj.__class__)
#         questions = QuestionSerializer(qs, many=True).data
#         return questions
#
#
# class QuestionLearnSerializer(ModelSerializer):
#     answers = SerializerMethodField()
#     statistics = SerializerMethodField()
#
#     class Meta:
#         model = QuestionModel
#         fields = [
#         #    'url',
#             'id',
#             'question',
#             'img_question',
#             'hint',
#             'test',
#             'statistics',
#             'answers'
#
#         ]
#
#     def get_answers(self, obj):
#         qs = AnswerModel.objects.filter(question=obj.id) #filter(content_type = obj.__class__)
#         answers = AnswerSerializer(qs, many=True).data
#         return answers
#
#     def get_statistics(self, obj):
#         qs = QuestionStatistic.objects.filter(question=obj.id) #filter(content_type = obj.__class__)
#         return QuestionStatisticSerializer(qs, many=True).data
