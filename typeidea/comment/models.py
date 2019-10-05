from django.db import models
from django.contrib.auth.models import User

from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='文章')
    content = models.CharField(max_length=2000, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='别名')
    websit = models.URLField(verbose_name='网址')
    email = models.EmailField(verbose_name='邮箱')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta():
        verbose_name = verbose_name_plural = '评论'

    def __str__(self):
        return '{}'.format(self.post.title)

    def nickname_show(self):
        return '来自{}的评论'.format(self.nickname)
    nickname_show.short_description = '评论者'

