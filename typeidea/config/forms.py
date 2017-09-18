# coding:utf-8
from __future__ import unicode_literals

from django import forms

from .models import Link, SideBar


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link


class SideBatForm(forms.ModelForm):
    class Meta:
        model = SideBar
