# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import UserInfo
# Create your views here.

def regist(request):

	if request.method == 'POST':
		username = request.POST.get('username', '')
		passwaord = request.POST.get('password', '')
		kind = request.POST.get('kind', '')
		phone = request.POST.get('phone', '')

		form = UserInfo()
		form.username = username
		form.password = password
		form.kind = kind
		form.phone = phone

		form.save()

	return render(request, 'regist.html')