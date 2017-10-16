# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    if category_id:
        # 分类页面
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        # 标签页面
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()

    context = {
        'posts': queryset,
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, pk=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("post does not exist")

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context=context)
