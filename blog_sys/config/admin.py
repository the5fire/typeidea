# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

# Register your models here.
from env_setting.custom_site import custom_site
from env_setting.custom_admin import BaseOwnerAdmin
from .models import Link, SideBar


@admin.register(Link, site=custom_site)
# class LinkAdmin(admin.ModelAdmin):
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'weight', 'owner', 'edit_operator')

    def edit_operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:config_link_change', args=(obj.id,))
        )
    edit_operator.short_description = '编辑'


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'content', 'content', 'owner', 'created_time')

