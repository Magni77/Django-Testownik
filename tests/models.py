from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
User = settings.AUTH_USER_MODEL


class AnswerModel(models.Model):
    answer = models.CharField(max_length=120, blank=True, null=True)
    img_answer = models.ImageField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __unicode__(self):
        return self.answer


class QuestionModel(models.Model):
    question = models.TextField()
    answers = models.ManyToManyField(AnswerModel, blank=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __unicode__(self):
        return self.question


class TestModel(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    questions = models.ManyToManyField(QuestionModel, blank=True)

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def get_absolute_url(self):
        return reverse("tests", kwargs={"id": self.id})

    def __unicode__(self):
        return self.title