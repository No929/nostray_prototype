# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import UserInfo, EmailVerifyRecord


class UserInfoAdmin(admin.ModelAdmin):
	pass


class EmailAdmin(admin.ModelAdmin):
	pass


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(EmailVerifyRecord, EmailAdmin)