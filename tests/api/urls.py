from django.conf.urls import url

from .views import TestListAPIView, QuestionListAPIView, TestDetailAPIView

urlpatterns = [
    url(r'^$', TestListAPIView.as_view(), name='list'),
    url(r'questions/', QuestionListAPIView.as_view(), name='questions'),
    url(r'^(?P<pk>\d+)/$', TestDetailAPIView.as_view(), name='testdetail'),


]
