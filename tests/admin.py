from django.contrib import admin
from .models import TestModel, QuestionModel, AnswerModel
# Register your models here.


class TestAdmin(admin.ModelAdmin):
    class Meta:
        model = TestModel


class QuestionsAdmin(admin.ModelAdmin):
    class Meta:
        model = QuestionModel


class AnswersAdmin(admin.ModelAdmin):
    class Meta:
        model = AnswerModel


admin.site.register(TestModel, TestAdmin)
admin.site.register(QuestionModel, QuestionsAdmin)
admin.site.register(AnswerModel, AnswersAdmin)
