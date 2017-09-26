# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.utils import override_settings
from django.db import connection
from .models import Auther, Book
# Create your tests here.

class TestAuthor(TestCase):
    def setUp(self):
        auth = Auther(name='zhangqian', age='23')
        auth.save()
        book = Book()
        book = Book(title='python', publisher='renmingongye')
        book.save()


    @override_settings(DEBUG=True)
    def test_filter(self):
        auth = Auther.objects.all()
        print auth
        book = Book.objects.all()
        print book
        print(connection.queries)
