from django.conf.urls import url, include
from django.contrib import admin

from .views import test_list

urlpatterns = [
    url(r'^$', test_list, name='list'),

]
