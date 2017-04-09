from django.conf.urls import url
from django.contrib.auth import get_user_model
from rest_framework import routers
from . import views
# from .views import (
#     LearningSessionViewSet,
#     LearningSessionListAPIView
#     )

User = get_user_model()
#
# router = routers.SimpleRouter()
# router.register(r'', LearningSessionViewSet)

urlpatterns = [
     url(r'^$', views.LearningSessionListAPIView.as_view(), name='learn-list'),
     url(r'^(?P<pk>\d+)/$', views.LearningSessionDetailAPIView.as_view(),
         name='learn-detail'),
     url(r'^(?P<pk>\d+)/statistics/$', views.StatisticsListAPIView.as_view(),
         name='learn-stats'),
     url(r'^(?P<pk>\d+)/statistics/(?P<pk_question>\d+)/$',
         views.StatisticsDetailAPIView.as_view(), name='learn-stats-detail'),
     url(r'^(?P<pk>\d+)/statistics/(?P<pk_question>\d+)/(?P<answer>correct|wrong)/$',
         views.StatisticsAnswerAPIView.as_view(), name='learn-stats-answer'),
#(?P<response>accept|reject)
    # url(r'^(?P<pk>\d+)/$', LearningSessionListAPIView.as_view(), name='learn-list'),

]

#urlpatterns += router.urls
