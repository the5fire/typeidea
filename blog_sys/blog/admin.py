# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag
from env_setting.custom_site import custom_site


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['title', 'owner']
    list_display = [
        'title',
        'category',
        'status',
        # 'tab',
        'created_time',
        'category',
    ]
    search_fields = ['']
    fieldsets = [
        ('TEST', {'fields': ['title', 'tag', 'owner'],}),
        ('CONTENT', {'fields': ['content', ], 'classes': ['collapse']}),
        ]


#custom_site.register(Post)


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['created_time', 'status']


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass

