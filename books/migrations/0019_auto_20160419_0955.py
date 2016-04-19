# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_book_ibook_link_volume_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cnx_id',
            field=models.CharField(blank=True, help_text='This is used to pull relevant information from CNX.', max_length=255, null=True),
        ),
    ]
