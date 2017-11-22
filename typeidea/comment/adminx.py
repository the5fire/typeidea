# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin

from .models import Comment


class CommentAdmin(object):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')

xadmin.site.register(Comment, CommentAdmin)
