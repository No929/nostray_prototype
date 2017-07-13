# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserInfo, EmailVerifyRecord
from .forms import LoginForm, RegisteForm


class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			user = UserInfo.objects.get(Q(phone=username)|Q(username=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None

# Create your views here.


class ActiveUserView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email
				user = UserInfo.objects.get(email=email)
				user.is_active = True
				user.save()
		return render(request, 'login.html')


class RegisteView(View):
	def get(self, request):
		registe_form = RegisteForm()
		return render(request, 'registe.html', {'registe_form':registe_form})

	def post(self, request):
		registe_form = RegisteForm(request.POST)
		if registe_form.is_valid():
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			kind = request.POST.get('kind', '')
			phone = request.POST.get('phone', '')

			form = UserInfo()
			form.username = username
			form.password = make_password(password)
			form.kind = kind
			form.phone = phone
			form.is_active = False

			form.save()
			return render(request, 'regist.html')
		else:
			pass


class VerifyUserView(View):
	def get(self, request):
		
		


class LoginView(View):
	def get(self, request):
		return render(request, "login.html", {})

	def post(self, request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'index.html')
				else:
					return render(request, 'login.html', {'msg':'用户名或密码错误！'}, {'login_form':login_form})
		else:
			return render(request, 'login.html', {'msg':'用户名或密码错误！'}, {'login_form':login_form})


def station(request):
	return render(request, 'station_list.html', {})