# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_studentinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='root',
            field=models.BooleanField(default=False),
        ),
    ]
