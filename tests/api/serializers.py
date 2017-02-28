from rest_framework.serializers import ModelSerializer, SerializerMethodField

from tests.models import TestModel, QuestionModel, AnswerModel


class TestSerializer(ModelSerializer):
    questions = SerializerMethodField()

    class Meta:
        model = TestModel
        fields = [
            'id',
            'user',
            'title',
            'description',
            'questions',
        ]

    def get_questions(self, obj):
        qs = QuestionModel.objects.filter(test=obj.id) #filter(content_type = obj.__class__)
        questions = QuestionSerializer(qs, many=True).data
        return questions


class QuestionSerializer(ModelSerializer):
    answers = SerializerMethodField()

    class Meta:
        model = QuestionModel

        fields = [
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
    class Meta:
        model = AnswerModel

        fields = [
            'id',
            'answer',
            'img_answer',
            'is_correct'

        ]

