# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_auto_20170206_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='lat',
            field=models.IntegerField(),
        ),
    ]
