from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        ReadOnlyField
                                        )

from tests.api.serializers import TestListSerializer, QuestionSerializer
from tests.models import QuestionModel
from .models import LearningSession, QuestionStatistic


class LearningSessionSerializer(ModelSerializer):
   # test = TestListSerializer()
    statistics = SerializerMethodField()
    correct_answers = SerializerMethodField()

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
      #  read_only_field = ['statistics']

    def get_statistics(self, obj):
        qs = QuestionStatistic.objects.filter(learning_session=obj.id)
        return QuestionStatisticSerializer(qs, many=True).data

    def create(self, validated_data):
        test_data = validated_data.pop('test')
        learn_obj = LearningSession.objects.create(**validated_data)
        questions_qs = QuestionModel.objects.filter(test=validated_data.test)
        for question in questions_qs:
            QuestionStatistic.objects.create(question=question, **test_data)
        return learn_obj

    def get_wrongs(self, obj):
        qs = QuestionStatistic.objects.filter(learning_session=obj.id)
        for q in qs:
            a = q.replies-q.attempts

    def get_correct_answers(self, obj):
        amount = 0
        qs = QuestionStatistic.objects.filter(learning_session=obj.id)
        for q in qs:
            amount += q.correct_answers
        return amount


class QuestionStatisticSerializer(ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = QuestionStatistic
        fields = [
            'id',
            'replies',
            'wrong_answers',
            'correct_answers',
            'question',
        ]
        read_only_field = ['question']


class QuestionStatisticDetailSerializer(ModelSerializer):

    class Meta:
        model = QuestionStatistic
        fields = [
            'id',
            'replies',
            'wrong_answers',
            'correct_answers',
            'question',
        ]
        read_only_field = ['question']


class LearningSessionCreateSerializer(ModelSerializer):

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
        read_only_fields = ['wrong_answers', 'correct_answers']

    def create(self, validated_data):
        test = validated_data['test']

        learn_session = LearningSession.objects.create(**validated_data)
        questions_qs = QuestionModel.objects.filter(test=test)
        for question in questions_qs:
            QuestionStatistic.objects.create(question=question,
                                             learning_session=learn_session)
        return learn_session


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