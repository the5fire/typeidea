from django import forms


class CommentAdminForms(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='内容', required=False)