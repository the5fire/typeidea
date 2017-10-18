# coding:utf-8

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = '张乾的博客'
    site_title = '管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
'''
custom_site.register(PostAdmin)
'''
