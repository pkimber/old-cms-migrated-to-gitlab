# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import block.models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20150809_2112'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='block', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Feature blocks',
                'verbose_name': 'Feature block',
            },
        ),
        migrations.CreateModel(
            name='FeatureBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name_plural': 'Blocks',
                'abstract': False,
                'verbose_name': 'Block',
            },
        ),
        migrations.CreateModel(
            name='FeatureStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Feature Styles',
                'ordering': ('name',),
                'verbose_name': 'Feature Style',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Headers',
                'verbose_name': 'Header',
            },
        ),
        migrations.CreateModel(
            name='HeaderBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name_plural': 'Blocks',
                'abstract': False,
                'verbose_name': 'Block',
            },
        ),
        migrations.CreateModel(
            name='HeaderStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Header styles',
                'ordering': ('name',),
                'verbose_name': 'Header style',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='carousel',
            field=models.ManyToManyField(to='block.Image'),
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.ForeignKey(to='block.Link', null=True, related_name='article_link', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='references',
            field=models.ManyToManyField(to='block.Link'),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ForeignKey(to='block.Image', null=True, related_name='picture', blank=True),
        ),
        migrations.AddField(
            model_name='header',
            name='block',
            field=models.ForeignKey(related_name='content', to='compose.HeaderBlock'),
        ),
        migrations.AddField(
            model_name='header',
            name='edit_state',
            field=models.ForeignKey(default=block.models._default_edit_state, to='block.EditState'),
        ),
        migrations.AddField(
            model_name='header',
            name='moderate_state',
            field=models.ForeignKey(default=block.models._default_moderate_state, to='block.ModerateState'),
        ),
        migrations.AddField(
            model_name='header',
            name='style',
            field=models.ForeignKey(to='compose.HeaderStyle', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='header',
            name='user_moderated',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='block',
            field=models.ForeignKey(related_name='content', to='compose.FeatureBlock'),
        ),
        migrations.AddField(
            model_name='feature',
            name='edit_state',
            field=models.ForeignKey(default=block.models._default_edit_state, to='block.EditState'),
        ),
        migrations.AddField(
            model_name='feature',
            name='moderate_state',
            field=models.ForeignKey(default=block.models._default_moderate_state, to='block.ModerateState'),
        ),
        migrations.AddField(
            model_name='feature',
            name='style',
            field=models.ForeignKey(to='compose.FeatureStyle', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='user_moderated',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='header',
            unique_together=set([('block', 'moderate_state')]),
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
