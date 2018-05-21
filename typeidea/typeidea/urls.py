import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page

from blog.apis import PostViewSet, CategoryViewSet
from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView, SearchView, AuthorView,
    Handler404, Handler50x
)
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from config.views import LinkListView
from comment.views import CommentView, VerifyCaptcha
from .autocomplete import CategoryAutocomplete, TagAutocomplete


handler404 = Handler404.as_view()
handler500 = Handler50x.as_view()

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^admin/', xadmin.site.urls, name='xadmin'),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', cache_page(60 * 20, key_prefix='sitemap_cache_')(sitemap_views.sitemap), {'sitemaps': {'posts': PostSitemap}}),
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^verify_captcha/', VerifyCaptcha.as_view(), name='verify_captcha'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
