from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField)

from tests.api.serializers import TestListSerializer, QuestionSerializer
from tests.models import QuestionModel
from .models import LearningSession, QuestionStatistic


class LearningSessionSerializer(ModelSerializer):
    test = TestListSerializer()
    statistics = SerializerMethodField()

    class Meta:
        model = LearningSession
        fields = [
            'id',
            'created',
            'updated',
            'is_active',
            'wrong_answers',
            'correct_answers',
            'test',
            'statistics',

        ]

    def get_statistics(self, obj):
        qs = QuestionStatistic.objects.filter(learning_session=obj.id) #filter(content_type = obj.__class__)
        return QuestionStatisticSerializer(qs, many=True).data

    def create(self, validated_data):
        test_data = validated_data.pop('test')
        learn_obj = LearningSession.objects.create(**validated_data)
        questions_qs = QuestionModel.objects.filter(test=validated_data.test)
        for question in questions_qs:
            QuestionStatistic.objects.create(question=question, **test_data)
        return learn_obj


class QuestionStatisticSerializer(ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = QuestionStatistic
        fields = [
            'replies',
            'attempts',
            'question',
        ]


class LearningSessionCreateSerializer(ModelSerializer):

    class Meta:
        model = LearningSession
        fields = [
            'user',
            'is_active',
            'test',
        ]

    def create(self, validated_data):
        test = validated_data['test']

       # test_data = validated_data.pop('test')
        learnSession = LearningSession.objects.create(**validated_data)
        questions_qs = QuestionModel.objects.filter(test=test)
        for question in questions_qs:
            QuestionStatistic.objects.create(question=question, learning_session = learnSession)
        print('smth')
        return learnSession


class LearningSessionListSerializer(ModelSerializer):
    class Meta:
        model = LearningSession
        fields = [
            'id',
            'user',
            'is_active',
            'test',
            'wrong_answers',
            'correct_answers'
        ]