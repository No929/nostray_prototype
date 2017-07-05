# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import UserInfo, EmailVerifyRecord


class UserInfoAdmin(admin.ModelAdmin):
	list_display = ['username', 'gender', 'kind', 'email', 'phone', 'creditrating']


class EmailAdmin(admin.ModelAdmin):
	list_display = ['code', 'email', 'send_type', 'send_time']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(EmailVerifyRecord, EmailAdmin)