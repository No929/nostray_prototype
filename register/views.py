# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse

from .models import UserInfo, EmailVerifyRecord
from .forms import LoginForm, RegisteForm, ForgetForm, ModifyPwdForm
from utils.email_send import emailVerify
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			user = UserInfo.objects.get(Q(email=username)|Q(username=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None

# Create your views here.


class RegisteView(View):
	def get(self, request):
		registe_form = RegisteForm()
		hashkey = CaptchaStore.generate_key()
		image_url = captcha_image_url(hashkey)
		return render(request, 'registe.html', {
			'registe_form':registe_form,
			'hashkey':hashkey,
			'image_url':image_url,
		})

	def post(self, request):
		captcha_refresh = request.POST.get('refresh', '')
		hashkey = CaptchaStore.generate_key()
		image_url = captcha_image_url(hashkey)

		if captcha_refresh == 'refresh':
			info = {'hashkey':hashkey, 'image_url':image_url}
			return JsonResponse(info, safe=False)

		registe_form = RegisteForm(request.POST)
		if registe_form.is_valid():
			username = request.POST.get('username', '')
			if UserInfo.objects.filter(username=username):
				return render(request, 'registe.html', {'msg':'用户已存在', 'registe_form':registe_form})
			password = request.POST.get('password', '')
			kind = request.POST.get('kind', '')
			email = request.POST.get('email', '')
			if UserInfo.objects.filter(email=email):
				return render(request, 'registe.html', {'msg':'邮箱已经注册', 'registe_form':registe_form})

			form = UserInfo()
			form.username = username
			form.password = make_password(password)
			form.kind = kind
			form.email = email
			form.is_active = False

			form.save()

			emailVerify(email, 'registe')
			return render(request, 'verify.html')
		else:
			return render(request, 'registe.html', {'registe_form':registe_form})


class ActiveUserView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email
				user = UserInfo.objects.get(email=email)
				user.is_active = True
				user.save()
		else:
			return render(request, 'active_fail.html')
		return render(request, 'actived.html')


class LoginView(View):
	def get(self, request):
		return render(request, "login.html")

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
					return render(request, 'login.html', {'msg':'账号未激活！', 'login_form':login_form})
			else:
				return render(request, 'login.html', {'msg':'用户名或密码错误！', 'login_form':login_form})
		else:
			return render(request, 'login.html', {'msg':'用户名或密码长度错误！', 'login_form':login_form})


class ForgetPwdView(View):
	def get(self, request):
		forget_form = ForgetForm()
		return render(request, 'forgetPass.html', {"forget_form":forget_form})

	def post(self, request):
		forget_form = ForgetForm(request.POST)
		if forget_form.is_valid():
			email = request.POST.get('email', '')
			emailVerify(email, 'forget')
			return render(request, 'send_success.html')
		else:
			return render(request, 'forgetPass.html', {"forget_form":forget_form})


class ResetPwdView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email
				return render(request, 'pwdreset.html', {'email':email})
		else:
			return render(request, 'active_fail.html')
		return render(request, 'actived.html')

	def post(self, request):
		modify_form = ModifyPwdForm(request.POST)
		if modify_form.is_valid():
			pwd1 = request.POST.get('password1', '')
			pwd2 = request.POST.get('password2', '')
			email = request.POST.get('email', '')
			if pwd1 != pwd2:
				return render(request, 'pwdreset.html', {'email':email, 'msg':'密码不一致'})
			user = UserInfo.objects.get(email=email)
			user.password = make_password(pwd1)
			user.save()

			return render(request, 'login.html')
		else:
			return render(request, 'pwdreset.html', {'modify_form':modify_form})


class ModifyPwdView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email
				return render(request, 'pwdreset.html', {'email':email})
		else:
			return render(request, 'active_fail.html')
		return render(request, 'actived.html')

	def post(self, request):
		modify_form = ModifyPwdForm(request.POST)
		if modify_form.is_valid():
			pwd1 = request.POST.get('password1', '')
			pwd2 = request.POST.get('password2', '')
			if pwd1 != pwd2:
				return render(request, 'pwdreset.html', {'email':email, 'msg':'密码不一致'})
			user = UserInfo.objects.get(email=email)
			user.password = make_password(password1)
			user.save()

			return render(request, 'login.html')
		else:
			return render(request, 'pwdreset.html', {'email':email, 'modify_form':modify_form})