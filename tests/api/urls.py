from django.conf.urls import url,include

from comments.views import TestCommentCreateAPIView
from .views import (
    TestListAPIView, QuestionListAPIView,
    TestDetailAPIView, QuestionDetailAPIView, AnswerDetailAPIView,
    TestCreateAPIView, QuestionCreateAPIView, AnswerCreateAPIView,
    TestUploadView, TestMarkAPIView, AnswersListAPIView, AverageMarkAPIView
    )


tests_patterns = [
    url(r'^$', TestListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TestDetailAPIView.as_view(), name='testDetail'),

    url(r'^create/', TestCreateAPIView.as_view(), name='createTest'),

    url(r'^(?P<pk>\d+)/questions/$', QuestionListAPIView.as_view()),
    url(r'^(?P<pk>\d+)/questions/(?P<question_id>\d+)/$', QuestionDetailAPIView.as_view()),

    url(r'^(?P<pk>\d+)/questions/(?P<question_id>\d+)/answers/$', AnswersListAPIView.as_view()),
    url(r'^(?P<pk>\d+)/questions/(?P<question_id>\d+)/answers/(?P<answer_id>\d+)/$', AnswerDetailAPIView.as_view()),

    url(r'^(?P<pk>\d+)/comments/$', TestCommentCreateAPIView.as_view(),
        {'type': 'test'}, name='test-comments'),
    url(r'^(?P<pk>\d+)/mark/$', TestMarkAPIView.as_view(), {'type': 'test'}, name='test-marks'),
    url(r'^(?P<pk>\d+)/mark/average/$', AverageMarkAPIView.as_view(), name='average-marks'),

]


urlpatterns = [
    url(r'^tests/', include(tests_patterns), name='tests_urls'),

    url(r'^questions/create/', QuestionCreateAPIView.as_view(), name='createQuestion'),
    url(r'^answers/create', AnswerCreateAPIView.as_view(), name='createAnswer'),

  #  url(r'^answers/(?P<pk>\d+)/$', AnswerDetailAPIView.as_view(), name='answerDetail'),

    url(r'^upload/$', TestUploadView.as_view(), name='upload'),

    url(r'^questions/(?P<pk>\d+)/comments/$', TestCommentCreateAPIView.as_view(),
        {'type': 'question'}, name='questions-comments'),

]

