# coding:utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site
from blog.views import (
    IndexView, CategoryView, TagView, PostView,
    AuthorView
)
# from config.views import links


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name="author"),
    # url(r'^links/$', links),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
