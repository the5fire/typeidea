# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pprint import pprint as pp

from django.contrib.auth.models import User
from django.db import connection
from django.db.models import F, Q, Count, Sum
from django.test import TestCase
from django.test.utils import override_settings

from .models import Category, Post


class TestCategory(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        self.user = user = User.objects.create_user('the5fire', 'fake@email.com', 'password')
        Category.objects.bulk_create([
            Category(name='cate_bulk_%s' % i, owner=user)
            for i in range(10)
        ])

    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.filter(
            (Q(id=1) & Q(id=2))
        )

        category = Category.objects.filter(id=1).update(status=F('status') + 1)

        user = User.objects.annotate(cate_sum=Sum('category__status')).get(username="the5fire")
        pp(connection.queries)

    def test_values(self):
        categories = Category.objects.values('name').filter(status=1)
        print(categories)

        categories = Category.objects.values_list('name')
        print(categories)

        categories = Category.objects.values_list('name', flat=True)
        print(categories)
        for cate_name in categories:
            print(cate_name)
