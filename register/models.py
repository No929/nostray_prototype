# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
	#主键自增
	#user_id = models.CharField(max_length=10, primary_key=True, verbose_name=u"主键ID")
	USER_KIND_CHOICES = [
		('A', u'Individual'),
		('B', u'Individual_plus'),
		('C', u'Station'),
		('D', u'Station_plus'),
		('E', u'Admin'),
	]
	username = models.CharField(max_length=16, null=True, blank=True, verbose_name=u"用户名")
	kind = models.CharField(max_length=1, choices=USER_KIND_CHOICES, verbose_name=u"用户类型")
	regtime = models.DateTimeField()
	last_update_time = models.DateField()
	phone = models.CharField(max_length=20, verbose_name=u"联系电话")
	email = models.EmailField(null=True, blank=True, verbose_name=u"邮箱")
	adress = models.CharField(max_length=45, null=True, blank=True, verbose_name=u"地址")
	icon = models.ImageField()
	creditrating = models.IntegerField()
	ip = models.IPAdressField()

	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name
		db_table = "user"
		ordering = "-user_id"