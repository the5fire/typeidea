# coding:utf-8
from __future__ import unicode_literals

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
