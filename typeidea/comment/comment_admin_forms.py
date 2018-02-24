# coding:utf-8
from django import forms


class CommentAdminForm(forms.ModelForm):
    #desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

    content = forms.CharField(widget=forms.Textarea,label="评论内容",required=True)