# -*- encoding: utf-8 -*-
from django.db import models

import reversion

from base.model_utils import TimeStampedModel
from base.singleton import SingletonModel
from block.models import (
    Page,
    PageSection,
    Section,
)


class HeaderFooter(SingletonModel):

    header = models.CharField(max_length=150)
    #footer_left = models.TextField(blank=True)
    #footer_right = models.TextField(blank=True)
    url_twitter = models.URLField(verbose_name='Twitter URL', blank=True)
    url_linkedin = models.URLField(verbose_name='LinkedIn URL', blank=True)
    url_facebook = models.URLField(verbose_name='Facebook URL', blank=True)

    class Meta:
        verbose_name = 'Header and footer'
        verbose_name_plural = 'Header and footers'

    def __str__(self):
        return '{}'.format(self.header)

reversion.register(HeaderFooter)


class TemplateManager(models.Manager):

    def create_template(self, template_name):
        template = self.model(template_name=template_name)
        template.save()
        return template

    def init_template(self, template_name):
        templates = self.model.objects.filter(template_name=template_name)
        if templates:
            result = templates[0]
        else:
            result = self.create_template(template_name)
        return result


class Template(TimeStampedModel):

    template_name = models.CharField(
        max_length=150,
        help_text="File name e.g. 'compose/page_article.html'",
    )
    objects = TemplateManager()

    class Meta:
        ordering = ('template_name',)
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __str__(self):
        return '{}'.format(self.template_name)

    def update_page(self, page):
        # iterate through existing sections in the page
        section_slugs = [s.section.slug for s in page.pagesection_set.all()]
        for slug in section_slugs:
            try:
                # if the section is still used on the page, then keep it.
                template_section = self.templatesection_set.get(
                    section__slug=slug
                )
            except TemplateSection.DoesNotExist:
                # if the section is not used on the page, then delete it.
                PageSection.objects.get(page=page, section__slug=slug).delete()
        # iterate through the new sections
        for template_section in self.templatesection_set.all():
            try:
                # if the section exists on the page, then keep it.
                PageSection.objects.get(
                    page=page, section=template_section.section
                )
            except PageSection.DoesNotExist:
                # if the section is not on the page, then add it.
                page_section = PageSection(
                    page=page,
                    section=template_section.section,
                )
                page_section.save()
        # update the page template name (if it has changed)
        if page.template_name == self.template_name:
            pass
        else:
            page.template_name = self.template_name
            page.save()

    def update_pages(self):
        for p in Page.objects.filter(template_name=self.template_name):
            self.update_page(p)

reversion.register(Template)


class TemplateSectionManager(models.Manager):

    def create_template_section(self, template, section):
        template_section = self.model(template=template, section=section)
        template_section.save()
        return template_section

    def init_template_section(self, template, section):
        try:
            template_section = self.model.objects.get(
                template=template,
                section=section,
            )
        except self.model.DoesNotExist:
            template_section = self.create_template_section(template, section)
        return template_section


class TemplateSection(TimeStampedModel):

    template = models.ForeignKey(Template)
    section = models.ForeignKey(Section, related_name='template_section_section')
    objects = TemplateSectionManager()

    class Meta:
        ordering = ('template__template_name', 'section__name')
        unique_together = ('template', 'section')
        verbose_name = 'Template section'
        verbose_name_plural = 'Template sections'

    def __str__(self):
        return '{}, {}'.format(self.template.template_name, self.section.name)

reversion.register(TemplateSection)
