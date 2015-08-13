# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def _header_footer(apps, schema_editor):
    cms = apps.get_model('cms', 'HeaderFooter')
    block = apps.get_model('block', 'HeaderFooter')
    obj = cms.objects.first()
    if obj:
        instance = block(**dict(
            header=obj.header,
            url_twitter=obj.url_twitter,
            url_linkedin=obj.url_linkedin,
            url_facebook=obj.url_facebook,
        ))
        instance.save()
        instance.full_clean()


def _template(apps, schema_editor):
    cms = apps.get_model('cms', 'Template')
    block = apps.get_model('block', 'Template')
    for obj in cms.objects.all():
        instance = block(**dict(
            template_name=obj.template_name,
        ))
        instance.save()
        instance.full_clean()


def _template_section(apps, schema_editor):
    cms = apps.get_model('cms', 'TemplateSection')
    block = apps.get_model('block', 'TemplateSection')
    block_section = apps.get_model('block', 'Section')
    block_template = apps.get_model('block', 'Template')
    for obj in cms.objects.all():
        template = block_template.objects.get(
            template_name=obj.template.template_name
        )
        slug = block_section.objects.get(
            slug=obj.section.slug
        )
        instance = block(**dict(
            template=template,
            section=section,
        ))
        instance.save()
        instance.full_clean()


def migrate_cms_to_block(apps, schema_editor):
    _header_footer(apps, schema_editor)
    _template(apps, schema_editor)
    _template_section(apps, schema_editor)


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_headerfooter_url_facebook'),
        ('block', '0004_auto_20150810_1651'),
    ]

    operations = [
        migrations.RunPython(migrate_cms_to_block),
    ]
