# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '\u5c55\u793a'), (2, '\u4e0b\u7ebf')], default=1, verbose_name='\u72b6\u6001'),
        ),
    ]
