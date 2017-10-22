# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


class CommonMixin(object):
    def get_context_data(self):
        categories = Category.objects.filter(status=1)  # TODO: fix magic number

        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)

        side_bars = SideBar.objects.filter(status=1)

        recently_posts = Post.objects.filter(status=1)[:10]
        # hot_posts = Post.objects.filte(status=1).order_by('views')[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]
        extra_context = {
            'nav_cates': nav_cates,
            'cates': cates,
            'side_bars': side_bars,
            'recently_comments': recently_comments,
            'recently_posts': recently_posts,
        }
        return super(CommonMixin, self).get_context_data(**extra_context)


class BasePostsView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasePostsView):
    pass


class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostsView):
    def get_queryset(self):
        tag_id = self.kwargs('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []

        posts = tag.posts.all()
        return posts


class PostView(CommonMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
