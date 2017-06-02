# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class UserInfo(models.Model):
	
	USER_KIND_CHOICES = [
		('A', u'Individual'),
		('B', u'Individual_plus'),
		('C', u'Station'),
		('D', u'Station_plus'),
	]
	SEX_CHOICES = [
		('MALE', 'male'),
		('FEMALE', 'female'),
		('SECRET', 'secret'),
	]
	user_id = models.AutoField(max_length=10, primary_key=True, verbose_name=u"用户主键ID")
	username = models.CharField(max_length=16, null=True, blank=True, verbose_name=u"用户名")
	sex = models.CharField(max_length=6, choices=SEX_CHOICES, verbose_name=u"性别")
	password = models.CharField(max_length=16,verbose_name=u"密码")
	introduce = models.CharField(max_length=100, verbose_name=u"介绍")
	kind = models.CharField(max_length=1, choices=USER_KIND_CHOICES, verbose_name=u"用户类型")
	mod_time = models.DateTimeField(auto_now_add=True, verbose_name="修订时间")
	add_time = models.DateTimeField(default=timezone.now, verbose_name=u"注册时间")
	phone = models.CharField(max_length=20, verbose_name=u"联系电话")
	email = models.EmailField(null=True, blank=True, verbose_name=u"邮箱")
	adress = models.CharField(max_length=45, null=True, blank=True, verbose_name=u"地址")
	icon = models.ImageField(upload_to='user_icon', null=True, verbose_name=u"头像")
	photo = models.ImageField(upload_to='user_photo', null=True, verbose_name=u"相册")
	creditrating = models.IntegerField(default=60, verbose_name=u"信誉评分")
	likes = models.IntegerField(default=0, verbose_name=u"顶")
	dislikes = models.IntegerField(default=0, verbose_name=u"踩")
	#ip = models.IPAdressField(null=True, blank=True, verbose_name=u"IP地址")

	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name
		db_table = "userinfo"
		ordering = ['-user_id']