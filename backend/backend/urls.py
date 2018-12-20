#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""backend URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from todoist import views


API_TITLE = 'Todoist API'
API_DESCRIPTION = 'A Web API for creating and viewing todolist.'
schema_view = get_schema_view(title=API_TITLE)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v01/', include('todoist.urls')),
    url(r'^api/v01/auth/', include('rest_framework.urls',
                                   namespace='rest_framework')),
    url(r'^api/v01/schema/$', schema_view),
    url(r'^api/v01/docs/', include_docs_urls(title=API_TITLE,
                                             description=API_DESCRIPTION, public=False))
]
