# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-14 19:13
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('pages', '0025_auto_20160712_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopters',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='adoptionform',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='give',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='products',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='productsallies',
            name='allies_ptr',
        ),
        migrations.RemoveField(
            model_name='productsallies',
            name='page',
        ),
        migrations.RemoveField(
            model_name='research',
            name='page_ptr',
        ),
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('tagline', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('person', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('position', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('biography', wagtail.wagtailcore.blocks.RichTextBlock())))), ('content_row', wagtail.wagtailcore.blocks.StreamBlock((('content_block', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('hidden', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('quote_block', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), icon='form')), ('list', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('description', wagtail.wagtailcore.blocks.RichTextBlock()), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))))),
        ),
        migrations.DeleteModel(
            name='Adopters',
        ),
        migrations.DeleteModel(
            name='AdoptionForm',
        ),
        migrations.DeleteModel(
            name='Give',
        ),
        migrations.DeleteModel(
            name='K12',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='ProductsAllies',
        ),
        migrations.DeleteModel(
            name='Research',
        ),
    ]
