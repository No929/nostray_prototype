# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=2, max_length=16)
	password = forms.CharField(required=True, min_length=6, max_length=16)


class RegisteForm(forms.Form):
	username = forms.CharField(required=True, min_length=2, max_length=16)
	password = forms.CharField(required=True, min_length=6, max_length=16)
	captcha = CaptchaField()