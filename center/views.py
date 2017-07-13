# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from utils.email_send import emailVerify
from register.models import UserInfo

# Create your views here.


def emailVerify(request):
	emailVerify(UserInfo.email, 'registe')