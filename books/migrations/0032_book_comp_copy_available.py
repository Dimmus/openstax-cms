# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0031_auto_20170330_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comp_copy_available',
            field=models.BooleanField(default=False),
        ),
    ]
