# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from django.urls import reverse
from django.utils.html import format_html
from xadmin.layout import Fieldset, Row

from .adminforms import PostAdminForm
from .models import Post, Category, Tag
from typeidea.adminx import BaseOwnerAdmin


class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        'title', 'category', 'status_show',
        'pv', 'uv', 'created_time', 'operator'
    ]
    list_display_links = []
    exclude = ('html', 'owner', 'pv', 'uv')

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    form_layout = (
        Fieldset(
            "基础信息",
            'title',
            'desc',
            Row('category', 'status', 'is_markdown'),
            'content',
            'tags',
        ),
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

xadmin.site.register(Post, PostAdmin)


class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = (
        'name', 'status',
        'is_nav',
    )

xadmin.site.register(Category, CategoryAdmin)


class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = (
        'name', 'status'
    )

xadmin.site.register(Tag, TagAdmin)
