from django.conf.urls import url
from django.contrib.auth import get_user_model
from rest_framework import routers

from .views import (
    LearningSessionViewSet,
    )

User = get_user_model()

router = routers.SimpleRouter()
router.register(r'', LearningSessionViewSet)

urlpatterns = [
    # url(r'^(?P<pk>\d+)/$', LearningSessionAPIView.as_view(), name='learn'),

]

urlpatterns += router.urls
