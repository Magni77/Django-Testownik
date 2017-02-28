from django.conf.urls import url

from .views import (
    TestListAPIView, QuestionListAPIView,
    TestDetailAPIView, QuestionDetailAPIView, AnswerDetailAPIView,
    TestCreateAPIView, QuestionCreateAPIView, AnswerCreateAPIView,
    TestEditAPIView, QuestionEditAPIView, AnswerEditAPIView,
    TestDeleteAPIView, QuestionDeleteAPIView, AnswerDeleteAPIView

    )

urlpatterns = [
    url(r'^$', TestListAPIView.as_view(), name='list'),
    url(r'questions/', QuestionListAPIView.as_view(), name='questions'),

    url(r'createtest/', TestCreateAPIView.as_view(), name='createTest'),
    url(r'createquestion/', QuestionCreateAPIView.as_view(), name='createQuestion'),
    url(r'createanswer/', AnswerCreateAPIView.as_view(), name='createAnswer'),

    url(r'^test/(?P<pk>\d+)/$', TestDetailAPIView.as_view(), name='testDetail'),
    url(r'^question/(?P<pk>\d+)/$', QuestionDetailAPIView.as_view(), name='questionDetail'),
    url(r'^answer/(?P<pk>\d+)/$', AnswerDetailAPIView.as_view(), name='answerDetail'),

    url(r'^test/(?P<pk>\d+)/edit/$', TestEditAPIView.as_view(), name='testEdit'),
    url(r'^question/(?P<pk>\d+)/edit/$', QuestionEditAPIView.as_view(), name='questionEdit'),
    url(r'^answer/(?P<pk>\d+)/edit/$', AnswerEditAPIView.as_view(), name='answerEdit'),

    url(r'^test/(?P<pk>\d+)/delete/$', TestDeleteAPIView.as_view(), name='testDelete'),
    url(r'^question/(?P<pk>\d+)/delete/$', QuestionDeleteAPIView.as_view(), name='questionDelete'),
    url(r'^answer/(?P<pk>\d+)/delete/$', AnswerDeleteAPIView.as_view(), name='answerDelete'),

]
