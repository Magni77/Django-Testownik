from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from tests.models import TestModel, QuestionModel

User = settings.AUTH_USER_MODEL
# Create your models here.


class LearningSession(models.Model):
    user = models.ForeignKey(User)
    test = models.ForeignKey(
        TestModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    wrong_answers = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)



          #  obj.save()
    # def clean(self):
    #     user_qs = LearningSession.objects.filter(user=self.user)
    #     #print(dir(user_qs.first().user))
    #     if len(user_qs) > 0:
    #         if self.user == user_qs.first().user:
    #             if self.test == user_qs.first().test:
    #                 raise ValidationError("This user has already.")
    #  #   print(user_qs.first().user)
    #  #   print(self.user)

    def __str__(self):
        return "{} session {}".format(self.user, self.test)


class QuestionStatistic(models.Model):
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.SET_NULL,
        null=True
    )

    learning_session = models.ForeignKey(LearningSession)
    replies = models.IntegerField(default=3)
    wrong_answers = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)

    def clean(self):
        user_qs = QuestionStatistic.objects.filter(
            question=self.question,
            learning_session=self.learning_session
        )
        if len(user_qs) > 0:
            if self.question == user_qs.first().question:
                if self.learning_session == user_qs.first().learning_session:
                    raise ValidationError("This question is alredy in session.")

    def __str__(self):
        return "{}  {}".format(self.question, self.learning_session)