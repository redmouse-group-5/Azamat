# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_auto_20170206_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='lat',
            field=models.CharField(max_length=120),
        ),
    ]
