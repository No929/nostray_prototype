# -*- coding: utf-8 -*-

from django import forms

from .models import Posts

class PostForm(forms.Form):
    title = forms.CharField(required=True, min_length=1, max_length=20)
    content = forms.CharField(required=True, min_length=1, max_length=2000)
    image = forms.ImageField(required=True)