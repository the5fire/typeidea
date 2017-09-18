# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Link, SideBar
from typeidea.custom_site import custom_site


@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'created_time',)
    list_filter = ('status',)
    search_fields = ('title', 'herf',)



@admin.register(SideBar, site=custom_site)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'display_type', 'created_time',)
    list_filter = ('status', 'display_type',)
    search_fields = ('title',)
