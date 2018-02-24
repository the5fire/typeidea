# coding:utf-8

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'
    

class CommentAdminSite(AdminSite):
    #import pdb;pdb.set_trace()
    site_header = 'Typeidea评论'
    site_title = '评论管理'
    index_title = "comment homepage"

class TagAdminSite(AdminSite):
    site_header = 'Typeidea Tag Management'
    site_title = '标签管理'

custom_site = CustomSite(name='cus_admin')

comment_admin_site = CommentAdminSite(name='comment_admin')

tag_admin_site = TagAdminSite(name='tag_admin')

