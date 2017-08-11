# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from register.models import UserInfo

# Create your views here.
def index(request):
	all_user = UserInfo.objects.all()
	user = all_user.get(username=request.user)

	return render(request, 'index.html', {
		"icon": user.icon,
		"user": user.username,
	})