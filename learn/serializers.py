from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        HyperlinkedIdentityField,
                                        EmailField,
                                        CharField,
                                        ValidationError)

from .models import LearningSession, QuestionStatistic
from accounts.serializers import UserBasicDetailsSerializer
from tests.api.serializers import TestListSerializer


class LearningSessionSerializer(ModelSerializer):
    user = UserBasicDetailsSerializer()
    test = TestListSerializer()
    statistics = SerializerMethodField()

    class Meta:
        model = LearningSession
        fields = [
            'id',
            'user',
            'created',
            'updated',
            'is_active',
            'test',
            'statistics'

        ]

    def get_statistics(self, obj):
        qs = QuestionStatistic.objects.filter(learning_session=obj.id) #filter(content_type = obj.__class__)
        return QuestionStatisticSerializer(qs, many=True).data


class QuestionStatisticSerializer(ModelSerializer):

    class Meta:
        model = QuestionStatistic
        fields = [
            'question',
            'replies'
        ]