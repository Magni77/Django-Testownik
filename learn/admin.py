from django.contrib import admin

from .models import LearningSession, QuestionStatistic


# Register your models here.


class QuestionStatAdmin(admin.TabularInline):
   # class Meta:
    model = QuestionStatistic


#admin.site.register(QuestionStatistic, QuestionStatAdmin)

class LearningSessionAdmin(admin.ModelAdmin):
    inlines = [QuestionStatAdmin]

    class Meta:
        model = LearningSession


admin.site.register(LearningSession, LearningSessionAdmin)
