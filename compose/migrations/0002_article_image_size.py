# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_size',
            field=models.CharField(max_length=3, choices=[('1-2', 'Half Width'), ('1-3', 'Third Width'), ('1-4', 'Quarter Width')], default='1-2'),
        ),
    ]
