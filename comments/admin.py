from django.contrib import admin
from .models import CommentModel


class CommentsAdmin(admin.ModelAdmin):
    class Meta:
        model = CommentModel


admin.site.register(CommentModel, CommentsAdmin)