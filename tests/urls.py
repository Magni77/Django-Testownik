from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from .views import  TestCreate, TestListView,  QuestionCreate, AnswerCreate,  upload_file

urlpatterns = [
    url(r'^$', TestListView.as_view(), name='list'),
    url(r'^createtest/$', TestCreate.as_view(), name='create'),
    url(r'^createquestion/$', QuestionCreate.as_view(), name='create'),
    url(r'^createanswer/$', AnswerCreate.as_view(), name='create'),
    url(r'^upload/$', upload_file, name='upload'),

]
