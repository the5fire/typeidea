# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
from env_setting.custom_site import custom_site
from env_setting.custom_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'nickname', 'website', 'email', 'created_time')
    search_fields = ['nickname', ]
