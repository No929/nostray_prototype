# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
	SEX_CHOICES = [
		('male', 'MALE'),
		('female', 'FEMALE'),
		('secret', 'SECRET'),
	]
	USER_KIND_CHOICES = [
		('个人', 'individual'),
		('救助站', 'station'),
		('团体组织', 'org'),
		('管理员', 'admin'),
	]
	gender = models.CharField(max_length=6, null=True, choices=SEX_CHOICES, verbose_name=u"性别", default="SECRET")
	kind = models.CharField(max_length=50, choices=USER_KIND_CHOICES , verbose_name=u"用户类型")
	phone = models.CharField(max_length=20, verbose_name=u"联系电话")
	introduce = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"介绍")
	adress = models.CharField(max_length=45, null=True, blank=True, verbose_name=u"地址")
	real_name = models.CharField(max_length=10, null=True, verbose_name=u"真实姓名")
	passport = models.CharField(max_length=50, null=True, verbose_name=u"身份证")
	icon = models.ImageField(upload_to='user_icon/%Y/%m', default="user_icon/default.png", max_length=100, verbose_name=u"头像")
	photo = models.ImageField(upload_to='user_photo/%Y/%m', default="user_photo/default.png",max_length=100, verbose_name=u"相册")
	creditrating = models.IntegerField(default=60, verbose_name=u"信誉评分")
	following = models.IntegerField(default=0, verbose_name=u"关注数")
	follower = models.IntegerField(default=0, verbose_name=u"被关注数")

	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.username

class EmailVerifyRecord(models.Model):
	SEND_TYPE_CHOICES = [
		("registe", u"注册"),
		("forget", u"找回密码"),
	]
	code = models.CharField(max_length=20, verbose_name=u"验证码")
	email = models.EmailField(max_length=50, verbose_name=u"邮箱")
	send_type = models.CharField(max_length=10, choices=SEND_TYPE_CHOICES, verbose_name=u"验证码类型")
	send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

	class Meta:
		verbose_name = u"邮箱验证码"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return '{0}({1})'.format(self.code, self.email)