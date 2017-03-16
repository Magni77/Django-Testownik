from django.conf.urls import url

from .views import (
    TestListAPIView, QuestionListAPIView,
    TestDetailAPIView, QuestionDetailAPIView, AnswerDetailAPIView,
    TestCreateAPIView, QuestionCreateAPIView, AnswerCreateAPIView,
    TestUploadView,
    )
from comments.views import TestCommentCreateAPIView

urlpatterns = [
    url(r'^tests/$', TestListAPIView.as_view(), name='list'),
    url(r'questions/$', QuestionListAPIView.as_view(), name='questions'),

    url(r'tests/create/', TestCreateAPIView.as_view(), name='createTest'),
    url(r'questions/create/', QuestionCreateAPIView.as_view(), name='createQuestion'),
    url(r'answers/create', AnswerCreateAPIView.as_view(), name='createAnswer'),

    url(r'^tests/(?P<pk>\d+)/$', TestDetailAPIView.as_view(), name='testDetail'),
    url(r'^questions/(?P<pk>\d+)/$', QuestionDetailAPIView.as_view(), name='questionDetail'),
    url(r'^answers/(?P<pk>\d+)/$', AnswerDetailAPIView.as_view(), name='answerDetail'),

    url(r'^upload/$', TestUploadView.as_view(), name='upload'),

    url(r'^tests/(?P<pk>\d+)/comments$', TestCommentCreateAPIView.as_view(), {'type': 'test'}, name='test-comments'),
    url(r'^questions/(?P<pk>\d+)/comments$', TestCommentCreateAPIView.as_view(), {'type': 'question'}, name='test-comments'),


]