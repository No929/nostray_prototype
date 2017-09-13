# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from register.models import UserInfo
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class Animal(View):

	def get(self, request):
		all = UserInfo.objects.all()
		all_stations = all.filter(kind='救助站')
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_stations, 12, request=request)
		stations = p.page(page)

		return render(request, "adopt.html", {
			'all_stations': stations,
		})


class Station(View):

	def get(self, request):
		pass