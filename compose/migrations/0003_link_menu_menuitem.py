# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20150419_2130'),
        ('compose', '0002_auto_20150806_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=512)),
                ('page', models.ForeignKey(to='block.Page', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Link',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('navigation', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'ordering': ('navigation', 'slug'),
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('link', models.ForeignKey(to='compose.Link', null=True, blank=True)),
                ('menu', models.ForeignKey(to='compose.Menu', null=True)),
                ('parent', models.ForeignKey(to='compose.MenuItem', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
                'ordering': ('order', 'title'),
            },
        ),
    ]
