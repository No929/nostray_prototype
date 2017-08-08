# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from community.views import AllPosts, PosterView, LikeView


urlpatterns =[
    url(r'^allpost/$', AllPosts.as_view(), name='allpost'),
    url(r'^poster/$', PosterView.as_view(), name='poster'),
    url(r'^like/$', LikeView.as_view(), name='like')
]