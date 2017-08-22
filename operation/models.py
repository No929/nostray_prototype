# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from register.models import UserInfo
#from animal.models import Animals
from community.models import Posts
# Create your models here.


class UserFavorite(models.Model):
	FAV_TYPE_CHOICES = [
		('animal', 1),
		('post', 2),
		('station', 3),
	]
	user = models.ForeignKey(UserInfo, verbose_name=u"用户")
	fav_id = models.IntegerField(default=0, verbose_name=u"数据ID")
	fav_type = models.IntegerField(choices=FAV_TYPE_CHOICES, default=1, verbose_name=u"收藏类型")

	class Meta:
		verbose_name = u"用户收藏"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.user.username

class UserMessage(models.Model):
	user = models.ForeignKey(UserInfo, verbose_name=u"接收用户")
	message = models.CharField(max_length=500, verbose_name=u"内容")
	has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
	add_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

	class Meta:
		verbose_name = u"用户消息"
		verbose_name_plural = verbose_name


class UserLikes(models.Model):
	user = models.ForeignKey(UserInfo, verbose_name=u"点赞用户")
	post_id = models.ForeignKey(Posts, verbose_name=u"点赞帖子id")

	class Meta:
		verbose_name = u"点赞信息"
		verbose_name_plural = verbose_name
