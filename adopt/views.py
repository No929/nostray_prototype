# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from register.models import UserInfo
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class ShowNearBy(View):

	def get(self, request):
		all_user = UserInfo.objects.all()
		user = all_user.get(username=request.user)

		all_stations = UserInfo.objects.filter(kind='station')
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_stations, 12, request=request)
		stations = p.page(page)

		return render(request, "adopt.html", {
			'icon': user.icon,
			'user': user.username,
			'all_stations': stations,
		})