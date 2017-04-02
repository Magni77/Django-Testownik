from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import CommentModel


class CommentDetailSerializer(serializers.ModelSerializer):
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = CommentModel
        fields = [
            'content',
            'date',
            'user',
          #  'content_object'
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = CommentModel
        fields = [
            'content',
            'date',
            'user',
            'content_type',
            'object_id'
        ]