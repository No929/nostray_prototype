# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from community.views import AllPosts


urlpatterns =[
    url(r'^allpost/$', AllPosts.as_view(), name='allpost'),
]