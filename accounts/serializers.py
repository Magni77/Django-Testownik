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
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
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
    password2 = CharField(max_length=15)

    def validate(self, attrs):
        data = self.get_initial()
        pwd1 = data.get('password')
        pwd2 = data.get('password2')
        if pwd1 != pwd2:
            raise ValidationError("Passwords must match.")

        if len(pwd1) < 8:
            raise ValidationError('Password too short')

        return attrs