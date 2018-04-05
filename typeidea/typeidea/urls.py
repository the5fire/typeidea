from django.conf.urls import url
from django.contrib import admin

from blog.views import post_list, post_detail
from config.views import links
from .custom_site import custom_site

urlpatterns = [
    url(r'^$', post_list, name='index'),
    url(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
    url(r'^links/$', links, name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin'),
]
