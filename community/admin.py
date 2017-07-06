# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Posts, Comments


class PostsAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'add_time', 'post_cate', 'animal_cate']
	search_fields = ['user', 'title', 'post_cate', 'animal_cate']
	list_filter = ['user__username', 'post_cate', 'animal_cate', 'add_time']


class CommentsAdmin(admin.ModelAdmin):
	list_display = ['post', 'user', 'add_time']
	search_fields = ['post', 'user']
	list_filter = ['post__title', 'user__username', 'add_time']


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)