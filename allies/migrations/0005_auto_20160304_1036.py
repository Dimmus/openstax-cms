# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allies', '0004_auto_20160224_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ally',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo', to='wagtailimages.Image'),
        ),
    ]