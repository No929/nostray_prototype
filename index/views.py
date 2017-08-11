# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from register.models import UserInfo

# Create your views here.
def index(request):
	if request.method == 'GET':
		all_user = UserInfo.objects.all()
		user = all_user.filter(username=request.user.username)
		return render(request, 'index.html', {
			"icon": user.icon,
			"user": user.username,
		})