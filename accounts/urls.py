from django.conf.urls import url
from django.contrib.auth import get_user_model
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import (
    UserCreateAPIView,
    UserViewSet
  #  UserDetailsAPIView
    )

User = get_user_model()


urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
]
router = routers.SimpleRouter()
router.register(r'', UserViewSet)

urlpatterns += router.urls

'''
curl -X GET http://127.0.0.1:8012/api/learn/all/ -H 'Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJvcmlnX2lhdCI6MTQ4ODgzMDM1OCwiZW1haWwiOiIiLCJpc19zdXBlcnVzZXIiOnRydWUsImV4cCI6MTQ4ODg0MDI1OH0.ZFsdEZZXZT8zeYOcP98MxuVVlSWPWWCy3mJ93H1gVbI'
'
curl -X POST -H "Content-Type: application/json" -d  '127.0.0.1:8012/api/learn/all/'  'Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODg5MjAyOTgsIm9yaWdfaWF0IjoxNDg4OTEwMzk4LCJlbWFpbCI6IiIsInVzZXJfaWQiOjMsInVzZXJuYW1lIjoiUmFkZWsifQ.8QKThLP0TjyliZwOC1nEHfDYeKnUq4hWdtRwszM2Q2M '



curl -H "Authorization: JWT .." http://127.0.0.1:8012/api/learn/all/


curl -X POST -d "username=Radek&password=radziogej" 127.0.0.1:8012/api/users/login/
"username=Radek&password=radziogej"


curl 127.0.0.1:8012/api/users/token-auth

curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODg5MjAxNDMsInVzZXJuYW1lIjoiUmFkZWsiLCJvcmlnX2lhdCI6MTQ4ODkxMDI0MywidXNlcl9pZCI6MywiZW1haWwiOiIifQ.G1wEbUUYDsRDHp2sYxsY-gygHaQv6Aya5HQnVdzu4UM", 'password': '123', 'password2': '4321' }' '127.0.0.1:8012/api/users/Radek/change-password/'



'''
