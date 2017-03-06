from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from django.contrib.auth import get_user_model
from rest_framework.authtoken import views
from .views import (
    UserCreateAPIView,
    UserDetailsAPIView
    )

User = get_user_model()


urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
#    url(r'^logout/$', UserLogOutAPIView.as_view(), name='logout'),
    url(r'^login/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),

    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailsAPIView.as_view(), name='user-detail'),

]


'''
curl -X GET http://127.0.0.1:8012/api/users/token-auth -H 'Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlJhZGVrIiwidXNlcl9pZCI6MywiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTQ4ODczMzYzNSwiZXhwIjoxNDg4NzMzOTM1fQ.DtigaZw7EQlv4SELjV1FH-iHdSpuFFjJRg08GBefoKw'
curl -X POST -H "Content-Type: application/json" '127.0.0.1:8012/api/users/logout/' 'Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IiIsImV4cCI6MTQ4ODczNDMxMSwidXNlcl9pZCI6Mywib3JpZ19pYXQiOjE0ODg3MzQwMTEsInVzZXJuYW1lIjoiUmFkZWsifQ.wykG9z_6ex2fUEsypwdIf6Uei1tjIM6OSqUZwkjaTwY'


curl -X POST -d "username=Radek&password=radziogej" 127.0.0.1:8012/api/users/login/
"username=Radek&password=radziogej"
curl 127.0.0.1:8012/api/users/token-auth

curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmlnX2lhdCI6MTQ4ODczNzE4MSwiZW1haWwiOiIiLCJleHAiOjE0ODg3NDcwODEsInVzZXJfaWQiOjMsInVzZXJuYW1lIjoiUmFkZWsifQ.55FN8SsKKab0xRjR4f4eb9cYnsoaNt4L2EVgdFxV8Q4"}' 127.0.0.1:8012/api/users/token-verify/
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmlnX2lhdCI6MTQ4ODczNzE4MSwiZW1haWwiOiIiLCJleHAiOjE0ODg3NDcwODEsInVzZXJfaWQiOjMsInVzZXJuYW1lIjoiUmFkZWsifQ.55FN8SsKKab0xRjR4f4eb9cYnsoaNt4L2EVgdFxV8Q4
'''
