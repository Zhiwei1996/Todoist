#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from todoist import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^todos/$', views.TodoList.as_view()),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
