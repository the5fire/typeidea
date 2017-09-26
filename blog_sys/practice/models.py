# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# coding: utf-8


class Book(models.Model):
    publisher = models.CharField(max_length=50, null=False, verbose_name='出版商')
    writter = models.ManyToManyField('Auther', verbose_name='著作人')
    title = models.CharField(max_length=30, verbose_name='书名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '书籍'


class Auther(models.Model):
    name = models.CharField(max_length=10, verbose_name='作者')
    age = models.IntegerField('年龄')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '著作人信息'
