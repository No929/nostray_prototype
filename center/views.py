# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from register.models import UserInfo


# Create your views here.

class CenterHome(View):

    def get(self, request, user_id):
        user = UserInfo.objects.get(id=int(user_id))


        return render(request, 'center_home.html', {})