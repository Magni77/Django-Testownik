from django.contrib import admin
from .models import LearningSession, QuestionStatistic
# Register your models here.


class LearningSessionAdmin(admin.ModelAdmin):
    class Meta:
        model = LearningSession


admin.site.register(LearningSession, LearningSessionAdmin)


class QuestionStatAdmin(admin.ModelAdmin):
    class Meta:
        model = QuestionStatistic


admin.site.register(QuestionStatistic, QuestionStatAdmin)