from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

User = settings.AUTH_USER_MODEL


def upload_location(instance, filename):
    return "%s/%s" %(instance.user, filename)


class TestModel(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    #TODO add test's rating
   # questions = models.ManyToManyField(QuestionModel, blank=True)

    # @property
    # def questions(self):
    #     return QuestionModel.objects.first()

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def get_absolute_url(self):
        return reverse("tests", kwargs={"id": self.id})

    @property
    def mark(self):
        queryset = TestMarkModel.objects.filter(test=self.id)
        qs = [x.mark for x in queryset]
        if len(qs) > 0:
            return sum(qs) / len(qs)
        return 0

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class QuestionModel(models.Model):
    user = models.ForeignKey(User, default=1)
    question = models.CharField(max_length=500, blank=True, null=True)
    img_question = models.ImageField(upload_to=upload_location, blank=True, null=True)
   # answers = models.ForeignKey(AnswerModel, blank=True)
    #answers = models.ManyToManyField(AnswerModel, blank=True)
    hint = models.TextField(blank=True, null=True)
    test = models.ForeignKey(TestModel, default=1)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question


class AnswerModel(models.Model):
    user = models.ForeignKey(User, default=1)
    answer = models.CharField(max_length=500, blank=True, null=True)
    img_answer = models.ImageField(upload_to=upload_location, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(QuestionModel, blank=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __unicode__(self):
        return self.answer

    def __str__(self):
        return self.answer


codes = (
    ('cp1250', 'Testownikowy'),
    ('utf-8', 'UTF-8')
    #  ('', 'Inny'),
)


class UploadFileModel(models.Model):
    test_choice = models.ForeignKey(TestModel, default=1)
    encoding = models.CharField(max_length=1, choices=codes)


class TestSettingsModel(models.Model):
    buffer = models.IntegerField()
    replies = models.IntegerField()


class TestMarkModel(models.Model):
    user = models.ForeignKey(User)
    mark = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])

    test = models.ForeignKey(TestModel, blank=True, related_name='testmark')