# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin

from .models import Link, SideBar
from typeidea.custom_site import tag_admin_site
from typeidea.custom_admin import BaseOwnerAdmin


@admin.register(Link, site=tag_admin_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time','operator')
    exclude = ('owner','status')

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑友情链接</a>',
            reverse('tag_admin:config_link_change', args=(obj.id,))
        )
    operator.short_description = '操作'
    


@admin.register(SideBar, site=tag_admin_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
