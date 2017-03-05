from django.db import models
from tests.models import TestModel, QuestionModel
# Create your models here.


class Learn(models.Model):
    testID = models.IntegerField()


class QuestionStatus(models.Model):
    questionID = models.IntegerField()
    learning_session = models.ForeignKey(Learn)
    replies = models.IntegerField(default=3)