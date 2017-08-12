# -*- coding: utf-8 -*-

from django import forms

from .models import Posts

class PostForm(forms.Form):
    image = forms.ImageField(required=False, max_length=100)
    title = forms.CharField(required=True, min_length=6, max_length=20)
    # content = forms.CharField(required=True, min_length=2, max_length=1000)
    #
    # class Meta:
    #     model = Posts
    #     fields = ['image', 'title', 'content']