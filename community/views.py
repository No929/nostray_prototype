# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from .models import Posts
from register.models import UserInfo
# Create your views here.


class AllPosts(View):
	def get(self, request):
		all_posts = Posts.objects.all()
		
		return render(request, 'community.html', {
			"all_posts":all_posts,
			})