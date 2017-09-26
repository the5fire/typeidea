# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase
from django.test.utils import override_settings

from .models import Category
from pprint import pprint as pp
# Create your tests here.


class TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user('zhangqian', 'qian.zhang@starcor.cn', 'passwd')
        user2 = User.objects.create_user('111111', '475131479@qq.com', 'test')
        for i in range(10):
            name = 'create_user_%s' % i
            if i == 5:
                a = Category(name='zhangqian', owner=user2)
                a.save()
                continue
            a = Category(name=name, owner=user)
            a.save()
        '''
        Category.objects.bulk_create([
            Category(name='create_bulk_%s' % i, owner=user) for i in range(10)
        ])
        for i in range(10):
            category_name = 'cate_%s' % i
            Category.objects.create(name=category_name, owner=user)
        '''
    @override_settings(DEBUG=True)
    def test_filter(self):
        '''
        queryset = Category.objects.filter(status=1).select_related('owner')
        for post in queryset:
            print(post.id, post.name, post.owner)
        pp(connection.queries)
        '''
        print [post.name for post in Category.objects.all()]
        pp(connection.queries)
        '''
        c = Category.objects.filter(owner__username='111111')
        print(c)
        pp(connection.queries)
        print(type(queryset))
        categories = queryset.order_by('?')
        print(categories)
        for i in categories:
            print i.id
        print categories.count()
        categories = categories.filter(status=1)
        print(categories.query)
        print(list(categories))
        print('-' * 10)
        pp(connection.queries)
        print('-' * 10)
        '''
