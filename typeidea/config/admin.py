from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Link, SideBar
from config.adminform import ConfigLinkAdminForm, ConfigSideBarAdminForm
from typeidea.custom_admin import BaseOwnerAdmin
from typeidea.custom_site import config_admin_site


@admin.register(Link, site=config_admin_site)
class LinkAdmin(BaseOwnerAdmin):
    # 展示页面定制
    list_display = [
        'title', 'href', 'weight', 'create_time', 'status_show', 'goahead_link'
    ]
    list_filter = ['title', 'create_time', 'weight']
    search_fields = ['title', 'weight']

    date_hierarchy = 'create_time'

    # 编辑页面定制
    form = ConfigLinkAdminForm
    save_on_top = False
    save_on_bottom = True
    fields = (
        'title', 'weight', 'status', 'href'
    )

    def goahead_link(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('config_admin:config_link_change', args=(obj.id,))
        )
    goahead_link.short_description = '链接'


@admin.register(SideBar, site=config_admin_site)
class SideBarAdmin(BaseOwnerAdmin):
    # 展示页面定制
    list_display = [
        'title', 'display_type', 'content', 'created_time', 'status_show'
    ]
    list_filter = ['title', 'created_time', 'display_type']
    search_fields = ['title', 'display_type', 'status']

    date_hierarchy = 'created_time'

    # 定义编辑页面
    form = ConfigSideBarAdminForm
    save_on_top = False
    save_on_bottom = True

    fields = (
        'title', 'display_type', 'content', 'status'
    )
