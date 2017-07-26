# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from register.models import UserInfo
# Create your models here.

class Posts(models.Model):
	POST_CATE_CHOICES = [
		('GV', 'giving'),
		('WT', 'want'),
		('NE', 'new_explorer'),
		('TS', 'tell_story'),
	]
	ANIMAL_CATE_CHOICES = [
		('DOG', 'dog'),
		('CAT', 'cat'),
		('OTHER', 'other'),
	]
	user = models.ForeignKey(UserInfo, related_name='user_name', verbose_name=u"所属用户")
	icon = models.ForeignKey(UserInfo, related_name='user_icon', verbose_name=u"用户头像")
	title = models.CharField(max_length=100, verbose_name=u"帖子标题")
	content = models.TextField(null=True, blank=True, verbose_name=u"帖子内容")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发帖时间")
	image = models.ImageField(max_length=100, upload_to='post_img/%Y/%m', null=True, verbose_name=u"贴图")
	post_cate = models.CharField(max_length=2, choices=POST_CATE_CHOICES, verbose_name="帖子类型")
	animal_cate = models.CharField(max_length=10, choices=ANIMAL_CATE_CHOICES, null=True, verbose_name="动物类型")
	comment_num = models.IntegerField(default=0, verbose_name=u"评论数量")
	likes = models.IntegerField(default=0, verbose_name=u"顶")
	dislikes = models.IntegerField(default=0, verbose_name=u"踩")

	class Meta:
		verbose_name = u"帖子"
		verbose_name_plural = verbose_name


class Comments(models.Model):
	post = models.ForeignKey(Posts, verbose_name=u"帖子")
	user = models.ForeignKey(UserInfo, verbose_name=u"所属用户")
	content = models.TextField(verbose_name=u"内容")
	image = models.ImageField(max_length=100, upload_to='comment_img/%Y/%m', null=True, verbose_name=u"评论图片")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")
	likes = models.IntegerField(default=0, verbose_name=u"顶")
	dislikes = models.IntegerField(default=0, verbose_name=u"踩")

	class Meta:
		verbose_name = u"评论"
		verbose_name_plural = verbose_name
