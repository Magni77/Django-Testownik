from rest_framework.serializers import ModelSerializer, SerializerMethodField

from tests.models import TestModel, QuestionModel, AnswerModel


class TestSerializer(ModelSerializer):
    quest = SerializerMethodField()

    class Meta:
        model = TestModel
        fields = [
            'id',
            'user',
            'title',
            'quest',
        ]

    def get_quest(self, obj):
        qs = QuestionModel.objects.filter(test = obj.id) #filter(content_type = obj.__class__)
        questions = QuestionSerializer(qs, many=True).data
        return questions


class QuestionSerializer(ModelSerializer):
    answ = SerializerMethodField()

    class Meta:
        model = QuestionModel

        fields = [
            'question',
            'img_question',
            'hint',
            'test',
            'answ'

        ]

    def get_answ(self, obj):
        qs = AnswerModel.objects.filter(question = obj.id) #filter(content_type = obj.__class__)
        answers = AnswerSerializer(qs, many=True).data
        return answers


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = AnswerModel

        fields = [
            'answer',
            'img_answer',
            'is_correct'

        ]