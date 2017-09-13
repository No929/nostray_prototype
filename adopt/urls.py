# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from adopt.views import Animal, Station


urlpatterns =[
    url(r'^animals/$', Animal.as_view(), name='animals'),
    url(r'^stations/$', Station.as_view(), name='stations'),
]