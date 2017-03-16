from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CommentModel


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            'content',
            'date',
            'user',
          #  'content_object'
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            'content',
            'date',
            'user',
            'content_type',
            'object_id'
        ]