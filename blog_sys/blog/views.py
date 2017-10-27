# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.db import connection
# Create your views here.
from .models import Post, Tag, Category
from pprint import pprint

def post_list(request, category_id=None, tag_id=None):
    page = request.GET.get('page', 1)
    page_size = 4
    try:
        Page = int(page)
    except TypeError:
        Page = 1

    PostData = Post.objects.all()
    if category_id:
        print category_id
        PostData = Post.objects.filter(category_id=category_id)
    elif tag_id:
        '''
        queryset = Post.objects.filter(tag=tag_id)
        '''
        PostData = Tag.objects.get(id=tag_id)
        if PostData:
            PostData = PostData.mytags.all()
        else:
            PostData = []
        #queryset = Post.objects.filter(tag=tag_id)
        #queryset = queryset.filter(tag_id=tag_id)
    paginator = Paginator(PostData, page_size)
    try:
        Posts = paginator.page(page)
    except EmptyPage:
        print paginator.num_pages
        Posts = paginator.page(paginator.num_pages)
    #for i in Posts:
    #    print i
    #print Posts.number
    #print dir(Posts)
    context = {
        'POST': Posts,
    }
    print connection.queries
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk=None):
    print '-----------------------'
    pprint(dir(request))
    pprint(pk)
    queryset = Post.objects.get(id=pk)
    pprint(queryset.title)
    print '-----------------------'
    context = {
        'post': queryset,
    }
    return render(request, 'blog/post_detail.html', context=context)
