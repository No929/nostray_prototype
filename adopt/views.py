# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from register.models import UserInfo

# Create your views here.


class ShowNearBy(View):

	def get(self, request):
		all_user = UserInfo.objects.all()
		user = all_user.get(username=request.user)
		return render(request, "adopt.html", {
			'icon': user.icon,
			'user': user.username,
		})