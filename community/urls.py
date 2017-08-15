# -*- coding: utf-8 -*-

from django.conf.urls import url

from community.views import AllPosts, PosterView, LikeView, ContentView


urlpatterns =[
    url(r'^allpost/$', AllPosts.as_view(), name='allpost'),
    url(r'^poster/$', PosterView.as_view(), name='poster'),
    url(r'^like/$', LikeView.as_view(), name='like'),
    url(r'^content/(?P<post_id>\d+)', ContentView.as_view(), name='content'),
]