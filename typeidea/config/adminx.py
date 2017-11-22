# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin

from .models import Link, SideBar
from typeidea.adminx import BaseOwnerAdmin


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')

xadmin.site.register(Link, LinkAdmin)


class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')

xadmin.site.register(SideBar, SideBarAdmin)
