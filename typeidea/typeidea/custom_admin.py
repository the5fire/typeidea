# coding:utf-8
from __future__ import unicode_literals

from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """ 所有有owner字段的admin模块的基类 """

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
