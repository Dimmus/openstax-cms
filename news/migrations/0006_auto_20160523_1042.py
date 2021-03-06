# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0012_copy_image_permissions_to_collections'),
        ('news', '0005_auto_20160523_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsarticle',
            old_name='intro',
            new_name='heading',
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='pin_to_top',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='subheading',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
