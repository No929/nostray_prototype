# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .models import UserInfo
# Create your views here.


def login(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username, password)
		if user is not None:
			login(request, user)
			return render(request, 'index.html')
		else:
			return render(request, 'index.html',{})
	elif request.method == 'GET':
		render(request, "login.html", {})

def regist(request):

	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		kind = request.POST.get('kind', '')
		phone = request.POST.get('phone', '')

		form = UserInfo()
		form.username = username
		form.password = password
		form.kind = kind
		form.phone = phone

		form.save()

	return render(request, 'regist.html')

def station(request):
	return render(request, 'station_list.html', {})