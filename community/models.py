# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Posts(models.Model):
	POST_CATE_CHOICES = [
		('FG', 'free_giving'),
		('FW', 'free_want'),
		('NE', 'new_explorer'),
		('TS', 'tell_story'),
	]
	ANIMAL_CATE_CHOICES = [
		('DOG', 'dog'),
		('CAT', 'cat'),
		('OTHER', 'other'),
	]
	post_id = models.AutoField(max_length=10, primary_key=True, verbose_name=u"帖子主键ID")
	title = models.CharField(max_length=20, verbose_name=u"帖子标题")
	content = models.CharField(max_length=512, null=True, blank=True, verbose_name=u"帖子内容")
	add_time = models.DateTimeField(default=timezone.now, verbose_name=u"发帖时间")
	mod_time = models.DateTimeField(auto_now_add=True, verbose_name=u"修订时间")
	image = models.ImageField(upload_to='post_img', null=True, verbose_name=u"贴图")
	user_id = models.IntegerField(verbose_name=u"所属用户")
	post_cate = models.CharField(max_length=2, choices=POST_CATE_CHOICES, verbose_name="帖子类型")
	animal_cate = models.CharField(max_length=10, choices=ANIMAL_CATE_CHOICES, null=True, verbose_name="动物类型")
	comments = models.IntegerField(default=0, verbose_name=u"评论数量")
	likes = models.IntegerField(default=0, verbose_name=u"顶")
	dislikes = models.IntegerField(default=0, verbose_name=u"踩")

	class Meta:
		verbose_name = u"帖子"
		verbose_name_plural = verbose_name
		db_table = "posts"
		ordering = ['-mod_time']


class Comments(models.Model):
	comment_id = models.AutoField(max_length=10, primary_key=True, verbose_name=u"评论id")
	content = models.CharField(max_length=256, verbose_name=u"内容")
	user_id = models.IntegerField(verbose_name=u"所属用户")
	image = models.ImageField(upload_to='comment_img', null=True, verbose_name=u"评论图片")
	add_time = models.DateTimeField(default=timezone.now, verbose_name=u"评论时间")
	likes = models.IntegerField(default=0, verbose_name=u"顶")
	dislikes = models.IntegerField(default=0, verbose_name=u"踩")

	class Meta:
		verbose_name = u"评论"
		verbose_name_plural = verbose_name
		db_table = "comments"
		ordering = ['-add_time']