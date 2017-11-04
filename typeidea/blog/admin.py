# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .adminforms import PostAdminForm
from .models import Post, Category, Tag
from typeidea.custom_site import custom_site
from typeidea.custom_admin import BaseOwnerAdmin


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        'title', 'category', 'status_show',
        'pv', 'uv', 'created_time', 'operator'
    ]
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = (
        ('category', 'title'),
        'desc',
        'status',
        ('content', 'is_markdown'),
        'html',
        'tags',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = (
        'name', 'status',
        'is_nav',
    )


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = (
        'name', 'status'
    )
