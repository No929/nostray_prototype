# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Posts, Comments


class PostsAdmin(admin.ModelAdmin):
	pass


class CommentsAdmin(admin.ModelAdmin):
	pass


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)