# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Banner


class BannerAdmin(admin.ModelAdmin):
	list_display = ['title', 'image', 'url', 'index', 'add_time']
	list_filter = ['title', 'add_time']


admin.site.register(Banner, BannerAdmin)