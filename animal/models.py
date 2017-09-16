# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from register.models import UserInfo

# Create your models here.


class Animals(models.Model):
	SPECIES_CHOICES = [
		('狗', 'dog'),
		('猫', 'cat'),
		('其他', 'other'),
	]
	SEX_CHOICES = [
		('公', 'male'),
		('母', 'female'),
	]
	IS_STRAY_CHOICE = [
		('否', 'no'),
		('是', 'yes'),
	]
	animal_id = models.AutoField(max_length=10, primary_key=True, verbose_name=u"动物编号")
	station_id = models.ForeignKey(UserInfo, verbose_name=u"救助站编号")
	name = models.CharField(max_length=10, null=True, verbose_name=u"动物名")
	sex = models.CharField(max_length=6, choices=SEX_CHOICES, verbose_name=u"性别")
	age = models.IntegerField(null=True, verbose_name=u"年龄")
	health = models.CharField(max_length=10, null=True, verbose_name=u"健康状况")
	price = models.CharField(max_length=10, default='免费', verbose_name=u"价格")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"入站日期")
	species = models.CharField(max_length=4, choices=SPECIES_CHOICES, verbose_name=u"物种")
	is_stray = models.CharField(max_length=3, choices=IS_STRAY_CHOICE, default='no', verbose_name=u"是否流浪")
	#dog_var = models.CharField(max_length=10, choices=DOG_CHOICES, null=True, verbose_name=u"狗品种")
	#cat_var = models.CharField(max_length=10, choices=CAT_CHOICES, null=True, verbose_name=u"猫品种")
	photo = models.ImageField(upload_to='animal_img/%Y/%m', null=True, verbose_name=u"动物图片")
	click_num = models.IntegerField(default=0, verbose_name=u"点击数")

	class Meta:
		verbose_name = u"动物信息"
		verbose_name_plural = verbose_name
