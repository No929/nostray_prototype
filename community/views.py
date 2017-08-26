# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Posts, Comments
from operation.models import UserFavorite, UserMessage, UserLikes
from register.models import UserInfo
from .forms import PostForm
from utils.imgResize import pImgResize
# Create your views here.


class AllPosts(View):

	def get(self, request):
		all_posts = Posts.objects.all()
		
		animal_kind = request.GET.get('animal', '')
		post_kind = request.GET.get('kind', '')
		if animal_kind:
			all_posts = all_posts.filter(animal_cate=animal_kind).order_by("-comment_num")
		if post_kind:
			all_posts = all_posts.filter(post_cate=post_kind).order_by("-comment_num")

		sort = request.GET.get('sort', '')
		if sort:
			if sort == 'add_time':
				all_posts = all_posts.order_by('-add_time')
			elif sort == 'comment_num':
				all_posts = all_posts.order_by('-comment_num')

		post_num = all_posts.count()

		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_posts, 7, request=request)
		posts = p.page(page)

		if request.user.is_authenticated():
			my_fav = UserFavorite.objects.all()
			my_fav_num = my_fav.filter(user=request.user).count()
			my_posts_num = all_posts.filter(user=request.user).count()
			my_msg = UserMessage.objects.all()
			my_msg_num = my_msg.filter(user=request.user, has_read=False).count()
			return render(request, 'community.html', {
				"all_posts" : posts,
				"post_num" : post_num,
				"animal_kind" : animal_kind,
				"post_kind" : post_kind,
				"sort" : sort,
				"my_fav_num" : my_fav_num,
				"my_posts_num" : my_posts_num,
				"my_msg_num" : my_msg_num,
			})
		else:
			my_fav_num = 0
			my_msg_num = 0
			my_posts_num = 0
			return render(request, 'community.html', {
				"all_posts" : posts,
				"post_num" : post_num,
				"animal_kind" : animal_kind,
				"post_kind" : post_kind,
				"sort" : sort,
				"my_fav_num" : my_fav_num,
				"my_posts_num" : my_posts_num,
			})


class LikeView(View):
	@login_required
	def post(self, request):
		pass


class PosterView(View):

	def post(self, request):
		if not request.user.is_authenticated:
			info = {'status':'fail', 'msg':'NO_LOGIN'}
			return JsonResponse(info, safe=False)
		poster_form = PostForm(request.POST)
		if poster_form.is_valid():
			title = request.POST.get('title')
			content = request.POST.get('content')
			post_cate = request.POST.get('post_cate')
			print request.POST.get('image', 'aaa')
			if 'image' in request.FILES:
				print 'bbb'
				img = request.FILES['image']
				url = pImgResize(img)
				post = Posts(title=title, content=content, image=url, post_cate=post_cate)
				post.save()
			else:
				print 'ccc'
				post = Posts(title=title, content=content, post_cate=post_cate)
				post.save()
			info = {'status':'success', 'msg':'成功'}
			return JsonResponse(info, safe=False)
		else:
			print 'ffff'
			info = {'status':'fail', 'msg':'失败'}
			return JsonResponse(info, safe=False)


class ContentView(View):

	def get(self, request, post_id):
		post = Posts.objects.get(id=int(post_id))
		post.click_num += 1
		post.save()
		all_comment = Comments.objects.all()
		comment = all_comment.filter(post=int(post_id))
		exist_fav = UserFavorite.objects.filter(user=post.user, fav_id=int(post_id), fav_type='post')

		return render(request, 'pContent.html', {
			'post' : post,
			'all_comment' : comment,
			'exist_fav' : exist_fav,
		})


class CommentView(View):
	def post(self, request):
		if not request.user.is_authenticated:
			info = {'status':'fail', 'msg':'NO_LOGIN'}
			return JsonResponse(info, safe=False)
		post = request.POST.get('post', 0)
		content = request.POST.get('content', '')
		print post
		print content
		if post and content:
			comment = Comments()
			comment.content = content
			comment.post = post
			comment.user = request.user
			comment.save()
			info = {'status':'success', 'msg':'发布成功'}
			return JsonResponse(info, safe=False)
		else:
			info = {'status':'fail', 'msg':'发布失败'}
			return JsonResponse(info, safe=False)


class PostFavView(View):

	def post(self, request):
		fav_id = request.POST.get('fav_id', '0')
		fav_type = request.POST.get('fav_type', '')

		if not request.user.is_authenticated:
			info = {'status':'fail', 'msg':'NO_LOGIN'}
			return JsonResponse(info, safe=False)

		exist_record = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)

		if exist_record:
			exist_record.delete()
			info = {'status':'fail', 'msg':'&hearts;&nbsp;收藏'}
			return JsonResponse(info, safe=False)
		else:
			user_fav = UserFavorite()
			if (fav_id > 0) and fav_type:
				user_fav.fav_id = fav_id
				user_fav.fav_type = fav_type
				user_fav.user = request.user
				user_fav.save()
				info = {'status':'success', 'msg':'已收藏'}
				return JsonResponse(info, safe=False)
			else:
				info = {'status':'fail', 'msg':'收藏失败'}
				return JsonResponse(info, safe=False)