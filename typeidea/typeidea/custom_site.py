from django.contrib.admin import AdminSite


class PostAdminSite(AdminSite):
    site_header = '文章管理'
    site_title = '文章管理后台'
    index_title = '首页'


class CommentAdminSite(AdminSite):
    site_header = '评论管理'
    site_title = '评论管理后台'
    index_title = '首页'


class ConfigAdminSite(AdminSite):
    site_header = '配置管理'
    site_title = '配置管理后台'
    index_title = '首页'


post_admin_site = PostAdminSite(name='post_admin')
comment_admin_site = CommentAdminSite(name='comment_amdin')
config_admin_site = ConfigAdminSite(name='config_admin')