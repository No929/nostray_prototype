# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserInfo


class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			user = UserInfo.objects.get(Q(email=username)|Q(phone=username)|Q(username=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None

# Create your views here.


def userLogin(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'index.html')
		else:
			return render(request, 'login.html', {'msg':'用户名或密码错误！'})
	elif request.method == 'GET':
		return render(request, "login.html", {})

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