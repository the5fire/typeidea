# coding:utf-8
from __future__ import unicode_literals

import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()
from django.conf.urls import url

from blog.views import (
    IndexView, CategoryView, TagView, PostView,
    AuthorView
)
from config.views import LinkView
from comment.views import CommentView
from typeidea import adminx  # NOQA
from .autocomplete import CategoryAutocomplete, TagAutocomplete


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name="author"),
    url(r'^links/$', LinkView.as_view(), name="links"),
    url(r'^comment/$', CommentView.as_view(), name="comment"),
    url(r'^admin/', xadmin.site.urls),
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
]
