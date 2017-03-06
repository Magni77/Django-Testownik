from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from django.contrib.auth import get_user_model
from rest_framework.authtoken import views
from .views import (
    LearningSessionAPIView,
    LearningSessionListAPIView
    )

User = get_user_model()


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', LearningSessionAPIView.as_view(), name='learn'),
    url(r'^all/$', LearningSessionListAPIView.as_view(), name='all'),


]