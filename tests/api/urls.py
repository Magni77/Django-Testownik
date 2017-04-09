from django.conf.urls import url, include
from comments.views import TestCommentCreateAPIView
from .views import (
    PublicTestListAPIView, QuestionListAPIView, PrivateTestListAPIView,
    TestDetailAPIView, QuestionDetailAPIView, AnswerDetailAPIView,
    TestCreateAPIView, QuestionCreateAPIView, AnswerCreateAPIView,
    TestUploadView, TestMarkAPIView, AnswersListAPIView, AverageMarkAPIView
    )

questions_patterns = [
    url(r'^$', QuestionListAPIView.as_view()),
    url(r'^(?P<question_id>\d+)/$',
        QuestionDetailAPIView.as_view()),
    url(r'^(?P<question_id>\d+)/answers/$',
        AnswersListAPIView.as_view()),
    url(r'^(?P<question_id>\d+)/answers/(?P<answer_id>\d+)/$',
        AnswerDetailAPIView.as_view()),

]

tests_patterns = [
    url(r'^$', PublicTestListAPIView.as_view(), name='list'),
    url(r'^private$', PrivateTestListAPIView.as_view(), name='private-list'),

    url(r'^(?P<pk>\d+)/questions/', include(questions_patterns),
        name='questions_url'),
    url(r'^(?P<pk>\d+)/$', TestDetailAPIView.as_view(), name='testDetail'),

    url(r'^create/', TestCreateAPIView.as_view(), name='createTest'),

    url(r'^(?P<pk>\d+)/comments/$', TestCommentCreateAPIView.as_view(),
        {'type': 'test'}, name='test-comments'),
    url(r'^(?P<pk>\d+)/mark/$', TestMarkAPIView.as_view(),
        {'type': 'test'}, name='test-marks'),
    url(r'^(?P<pk>\d+)/mark/average/$', AverageMarkAPIView.as_view(),
        name='average-marks'),

]


urlpatterns = [
    url(r'^tests/', include(tests_patterns), name='tests_urls'),

    url(r'^questions/create/', QuestionCreateAPIView.as_view(),
        name='createQuestion'),
    url(r'^answers/create', AnswerCreateAPIView.as_view(),
        name='createAnswer'),


    url(r'^upload/$', TestUploadView.as_view(), name='upload'),

    url(r'^questions/(?P<pk>\d+)/comments/$',
        TestCommentCreateAPIView.as_view(),
        {'type': 'question'}, name='questions-comments'),

]
