# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0007_externaldocumentation_internaldocumentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errata',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]