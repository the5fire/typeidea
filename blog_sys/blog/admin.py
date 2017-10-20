# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

# Register your models here.
from .models import Post, Category, Tag
from env_setting.custom_site import custom_site
from env_setting.custom_admin import BaseOwnerAdmin
from .adminforms import PostAdminForm

from pprint import pprint


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title',
        'category',
        'get_tag',
        'show_status',
        'owner',
        'created_time',
        'edit_operator',
    ]
#    list_display_links = ['category', 'edit_operator']
    list_display_links = []
    # list_editable = ['title']
    search_fields = ['category__name']
    # 动作栏位置
    actions_on_top = True
    # 动作栏后的统计计数器
    actions_selection_counter = True
    # 头部时间筛选栏
    date_hierarchy = 'created_time'

    # 编辑页面 #
    # 文章保存、退出栏位置, 默认为底部
    save_on_top = True
    # save_on_bottom = False
    filter_horizontal = ('tag',)
    fieldsets = [
        ('基础信息', {'fields': [('title', 'category'), 'status', 'tag', 'describe'], }),
        ('文章内容', {'fields': ['content', ], 'classes': ['collapse', ]}),
    ]

    def get_tag(self, obj):
        '''
        组织外键:post.tag
        '''
        return '、'.join([Mobj.name for Mobj in obj.tag.all()])
    get_tag.short_description = '标签'

    # 大写title
    # def upper_title(self, obj):
    #     return ('%s' % obj.created_time).upper()
    # upper_title.short_description = '自定义'

    def edit_operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    # edit_operator.allow_tags = True    已废弃，当返回不采用format_html时进行url转义
    edit_operator.short_description = '操作'

    def show_status(self, obj):
        if obj.status == 1:
            return '正常'
        else:
            return '异常'
    show_status.short_description = '状态'

    # 通过BaseOwnerAdmin改写
    # def save_model(self, request, obj, form, change):
    #    print(self, request, obj, form, change)
    #    #import pdb;pdb.set_trace()
    #    obj.owner = request.user

    #    return super(PostAdmin, self).save_model(request, obj, form, change)
# custom_site.register(Post)


class PostInlineAdmin(admin.TabularInline):
    fields = ('title', 'status')
    extra = 3
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [
        PostInlineAdmin,
    ]
    list_display = ['name', 'created_time', 'status']


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner']
    fields = ('name', 'status')
