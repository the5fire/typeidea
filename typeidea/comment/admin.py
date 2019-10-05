from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Comment
from .adminform import CommentAdminForms
from typeidea.custom_site import comment_admin_site
from typeidea.custom_admin import BaseOwnerAdmin

@admin.register(Comment, site=comment_admin_site)
class CommentAdmin(admin.ModelAdmin):
    # 展示页面定制
    list_display = [
        'post', 'content', 'nickname_show',
        'email', 'created_time', 'open_comment_website'
    ]
    list_filter = ['nickname', 'post', 'created_time']
    search_fields = ['nickname', 'post']

    date_hierarchy = 'created_time'

    # 编辑页面定制
    form = CommentAdminForms
    save_on_top = False
    save_on_bottom = True
    fields = (
        ('post', 'nickname'),
        'email',
        'content', 'websit'
    )
    

    def open_comment_website(self, obj):
        return format_html(
            '<a href={}>跳转至评论页</a>',
            reverse('comment_amdin:comment_comment_change', args=(obj.id,))
            )
    open_comment_website.short_description = '评论页'


class CommentInlineAdmin(admin.TabularInline):
    fields = ('nickname','content')
    extra = 1
    model = Comment
