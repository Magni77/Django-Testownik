from django.conf.urls import url
from .views import CreateCommentAPIView, TestListAPIView

urlpatterns = [
  #   url(r'^create/', CreateCommentAPIView, name='create-comment'),
     url(r'^$', TestListAPIView.as_view(), name='comments')

    # url(r'^token-refresh/', refresh_jwt_token),
    # url(r'^token-verify/', verify_jwt_token),
]