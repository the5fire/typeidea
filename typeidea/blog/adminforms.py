# coding:utf-8

from ckeditor.widgets import CKEditorWidget
from dal import autocomplete
from django import forms

from .models import Category, Tag


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    content = forms.CharField(widget=CKEditorWidget(), label="内容")
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )
