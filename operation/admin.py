# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import UserFavorite, UserMessage


class FavoriteAdmin(admin.ModelAdmin):
	pass


class MessageAdmin(admin.ModelAdmin):
	pass


admin.site.register(UserFavorite, FavoriteAdmin)
admin.site.register(UserMessage, MessageAdmin)