# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from adopt.views import ShowNearBy


urlpatterns =[
    url(r'^market/$', ShowNearBy.as_view(), name='market'),
]