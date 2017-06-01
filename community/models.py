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
		(),
		(),
		(),
		(),
	]
	post_id = models.AutoField(max_length=10, primary_key=True, verbose_name=u"帖子主键ID")
	title = models.CharField(max_length=20, verbose_name=u"帖子标题")
	content = models.CharField(max_length=512, null=True, blank=True, verbose_name=u"帖子内容")
	add_time = models.DateTimeField(default=timezone.now, verbose_name=u"发帖时间")
	mod_time = models.DateTimeField(auto_now_add=True, verbose_name=u"修订时间")
	image = models.ImageField(upload_to='post_img', null=True, verbose_name=u"贴图")
	user_id = models.IntegerField(verbose_name=u"所属用户")
	post_cate = models.CharField(max_length=2, verbose_name="帖子类型")
	animal_cate = models.CharField(max_length=10, null=True, verbose_name="动物类型")

	class Meta:
		verbose_name = u"帖子"
		verbose_name_plural = verbose_name
		db_table = "post"
		ordering = "-mod_time"