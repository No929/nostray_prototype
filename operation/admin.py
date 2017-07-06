# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import UserFavorite, UserMessage


class FavoriteAdmin(admin.ModelAdmin):
	list_display = ['user', 'fav_id', 'fav_type']
	search_fields = ['user', 'fav_type']
	list_filter = ['user__username', 'fav_type']


class MessageAdmin(admin.ModelAdmin):
	list_display = ['user', 'has_read', 'add_time']
	search_fields = ['user', 'message']
	list_filter = ['user', 'has_read', 'add_time']


admin.site.register(UserFavorite, FavoriteAdmin)
admin.site.register(UserMessage, MessageAdmin)