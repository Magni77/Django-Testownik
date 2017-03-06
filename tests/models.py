from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

User = settings.AUTH_USER_MODEL


def upload_location(instance, filename):
    return "%s/%s" %(instance.user, filename)


# class TestMenager(models.ManyToManyField):
#     def filter_by_instance(self, instance):
#         content_type = QuestionModel.objects.get_for_model(instance.__class__)
#         obj_id = instance.id
#         qs = super(QuestionModel, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
#         return qs


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

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class QuestionModel(models.Model):
    user = models.ForeignKey(User, default=1)
    question = models.TextField(blank=True, null=True)
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
    answer = models.TextField(blank=True, null=True)
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


