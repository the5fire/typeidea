# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render

from .models import Post, Tag, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    page = request.GET.get('page', 1)
    page_size = 4
    try:
        page = int(page)
    except TypeError:
        page = 1

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

    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.filter(status=1)  # TODO: fix magic number

    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    context = {
        'posts': posts,
        'nav_cates': nav_cates,
        'cates': cates,
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
