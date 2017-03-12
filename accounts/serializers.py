from django.contrib.auth import get_user_model
from rest_framework.serializers import (ModelSerializer,
                                        Serializer,
                                        SerializerMethodField,
                                        EmailField,
                                        CharField,
                                        ValidationError)

from learn.models import LearningSession
from learn.serializers import LearningSessionListSerializer
from tests.api.serializers import TestListSerializer
from tests.models import TestModel

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }

    def validate_email(self, value):
        data = self.get_initial()
        email = value

        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def create(self, data):
        username = data['username']
        email = data['email']
        password = data['password']
        user_obj = User(
                username = username,
                email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return data


class UserBasicDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class UserDetailSerializer(ModelSerializer):
    token = CharField(read_only=True)
    user_tests = SerializerMethodField()
    user_sessions = SerializerMethodField()
   # lookup_field = 'username'

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'token',
            'first_name',
            'last_name',
            'department',
            'specialization',
            'user_tests',
            'user_sessions',
        ]

    def get_user_tests(self, obj):
        qs = TestModel.objects.filter(user=obj.id) #filter(content_type = obj.__class__)
        return TestListSerializer(qs, many=True).data

    def get_user_sessions(self, obj):
        qs = LearningSession.objects.filter(user=obj.id) #filter(content_type = obj.__class__)
        return LearningSessionListSerializer(qs, many=True).data


class PasswordSerializer(Serializer):
    password = CharField(max_length=15)

    def validate(self, attrs):
        data = self.get_initial()
        pwd1 = data.get('password')

        if len(pwd1) < 7:
            raise ValidationError('Password too short')

        return attrs