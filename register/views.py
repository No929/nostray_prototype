# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import UserInfo
# Create your views here.

def regist(request):

	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		if request.POST.get('kind', '') == '救助站':
			kind = 'Station'
		elif request.POST.get('kind', '') == '个人':
			kind = 'Individual'
		else:
			kind = 'Orgnization'

		phone = request.POST.get('phone', '')

		form = UserInfo()
		form.username = username
		form.password = password
		form.kind = kind
		form.phone = phone

		form.save()

	return render(request, 'regist.html')