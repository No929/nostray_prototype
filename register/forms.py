# -*- coding: utf-8 -*-

from django import forms
import re
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=2, max_length=16)
	password = forms.CharField(required=True, min_length=6, max_length=16)


class RegisteForm(forms.Form):
	username = forms.CharField(required=True, min_length=2, max_length=16)
	password = forms.CharField(required=True, min_length=6, max_length=16)
	email = forms.EmailField(required=True)
	kind = forms.CharField(required=True, min_length=2, max_length=4)
	captcha = CaptchaField()

	def clean(self):
		try:
			captcha_x = self.cleaned_data('captcha')
		except Exception as e:
			print 'exception: ' + str(e)
			raise forms.ValidationError(u"验证码有误")

		return self.cleaned_data


class ForgetForm(forms.Form):
	email = forms.EmailField(required=True)
	captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ModifyPwdForm(forms.Form):
	password1 = forms.CharField(required=True, min_length=6, max_length=16)
	password2 = forms.CharField(required=True, min_length=6, max_length=16)