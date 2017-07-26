# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Posts
from register.models import UserInfo
# Create your views here.


class AllPosts(View):
	def get(self, request):
		all_posts = Posts.objects.all()
		
		animal_kind = request.GET.get('animal', '')
		post_kind = request.GET.get('kind', '')
		if animal_kind and post_kind:
			all_posts = all_posts.filter(animal_cate=animal_kind, post_cate=post_kind)

		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_posts, 7, request=request)
		posts = p.page(page)

		return render(request, 'community.html', {
			"all_posts" : posts,
			"animal_kind" : animal_kind,
			"post_kind" : post_kind,
			})