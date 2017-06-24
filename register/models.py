# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
import django.utils.timezone as timezone

from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
	SEX_CHOICES = [
		('MALE', 'male'),
		('FEMALE', 'female'),
		('SECRET', 'secret'),
	]
		
	nickname = models.CharField(max_length=16, verbose_name=u"昵称", default="")
	gender = models.CharField(max_length=6, null=True, choices=SEX_CHOICES, verbose_name=u"性别", default="SECRET")
	kind = models.CharField(max_length=100, verbose_name=u"用户类型")
	phone = models.CharField(max_length=20, verbose_name=u"联系电话")
	introduce = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"介绍")
	adress = models.CharField(max_length=45, null=True, blank=True, verbose_name=u"地址")
	icon = models.ImageField(upload_to='user_icon/%Y/%M',default=u"user_icon/default.png", max_length=100, verbose_name=u"头像")
	photo = models.ImageField(upload_to='user_photo/%Y/%M', default=u"user_photo/default.jpg", max_length=100, verbose_name=u"相册")
	creditrating = models.IntegerField(default=60, verbose_name=u"信誉评分")

	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.username

class EmailVerifyRecord(models.Model):
	SEND_TYPE_CHOICES = [
		("regist", u"注册"),
		("forget", u"找回密码"),
	]
	code = models.CharField(max_length=20, verbose_name=u"验证码")
	email = models.EmailField(max_length=50, verbose_name=u"邮箱")
	send_type = models.CharField(max_length=10, choices=SEND_TYPE_CHOICES)
	send_time = models.DateTimeField(default=datetime.now)

	class Meta:
		verbose_name = u"邮箱验证码"
		verbose_name_plural = verbose_name