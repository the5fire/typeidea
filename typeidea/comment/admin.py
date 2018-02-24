# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
from typeidea.custom_site import comment_admin_site
from .comment_admin_forms import CommentAdminForm

@admin.register(Comment, site=comment_admin_site)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ('content','post', 'nickname',  'website', 'created_time')
    list_display_links = ('content','post','nickname')
    search_fields = ('content','post__title','post__content','post__category__name')
    list_filter = ('content','post')
    fields = (('content','post'),'nickname')

    action_on_top = True
    action_on_bottom = True

    date_hierarchy = 'created_time'

    list_editable = ('website',)
