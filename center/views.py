# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from register.models import UserInfo
# Create your views here.

def showInfo(request):
	login_user = 
	userinfo = UserInfo.objects.filter(username=)