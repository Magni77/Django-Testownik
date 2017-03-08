from django.contrib import admin
from .models import TestModel, QuestionModel, AnswerModel
# Register your models here.


class TestAdmin(admin.ModelAdmin):
    class Meta:
        model = TestModel


class AnswersAdmin(admin.TabularInline):
    model = AnswerModel


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswersAdmin]

    class Meta:
        model = QuestionModel





admin.site.register(TestModel, TestAdmin)
admin.site.register(QuestionModel, QuestionsAdmin)
#admin.site.register(AnswerModel, AnswersAdmin)

