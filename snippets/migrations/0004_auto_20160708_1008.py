# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 15:08
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_delete_communityresource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyresource',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentresource',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
    ]
