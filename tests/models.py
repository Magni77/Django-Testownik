from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
User = settings.AUTH_USER_MODEL


class TestModel(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=150)
   # questions = models.ManyToManyField(QuestionModel, blank=True)

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def get_absolute_url(self):
        return reverse("tests", kwargs={"id": self.id})

    def __unicode__(self):
        return self.title


class QuestionModel(models.Model):
    user = models.ForeignKey(User, default=1)
    question = models.TextField()
    txt_question = models.FileField(blank=True, null=True)
   # answers = models.ForeignKey(AnswerModel, blank=True)
    #answers = models.ManyToManyField(AnswerModel, blank=True)
    hint = models.TextField(blank=True, null=True)
    test = models.ForeignKey(TestModel, default=1)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __unicode__(self):
        return self.question


class AnswerModel(models.Model):
    user = models.ForeignKey(User, default=1)
    answer = models.CharField(max_length=120, blank=True, null=True)
    img_answer = models.ImageField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(QuestionModel, blank=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __unicode__(self):
        return self.answer


