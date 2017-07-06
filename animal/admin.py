# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Animals


class AnimalsAdmin(admin.ModelAdmin):
	list_display = ['animal_id', 'station_id', 'name', 'sex', 'health', 'species']
	search_fields = ['animal_id', 'station_id', 'name', 'sex', 'health', 'species']
	list_filter = ['sex', 'health', 'species']


admin.site.register(Animals, AnimalsAdmin)