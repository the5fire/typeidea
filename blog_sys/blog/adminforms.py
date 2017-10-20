# coding: utf-8

from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='是否删除', required=False)  # TODO:处理布尔类型为我们需要的字段
    describe = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    # def __unicode__(self):
    #     return self.status

    def clean_status(self):
        if self.cleaned_data['status']:
            return 2
        else:
            return 1
