# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import block.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0003_auto_20150419_2130'),
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='block')),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Feature block',
                'verbose_name_plural': 'Feature blocks',
            },
        ),
        migrations.CreateModel(
            name='FeatureBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
            },
        ),
        migrations.CreateModel(
            name='FeatureStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Feature Style',
                'verbose_name_plural': 'Feature Styles',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Headers',
            },
        ),
        migrations.CreateModel(
            name='HeaderBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
            },
        ),
        migrations.CreateModel(
            name='HeaderStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Header style',
                'verbose_name_plural': 'Header styles',
            },
        ),
        migrations.AddField(
            model_name='header',
            name='block',
            field=models.ForeignKey(to='compose.HeaderBlock', related_name='content'),
        ),
        migrations.AddField(
            model_name='header',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='header',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='header',
            name='style',
            field=models.ForeignKey(to='compose.HeaderStyle', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='user_moderated',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='feature',
            name='block',
            field=models.ForeignKey(to='compose.FeatureBlock', related_name='content'),
        ),
        migrations.AddField(
            model_name='feature',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='feature',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='feature',
            name='style',
            field=models.ForeignKey(to='compose.FeatureStyle', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='user_moderated',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+'),
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
