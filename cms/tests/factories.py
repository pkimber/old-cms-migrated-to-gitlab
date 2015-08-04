# -*- encoding: utf-8 -*-
import factory

from block.tests.factories import SectionFactory
from cms.models import (
    CodeSnippet,
    Template,
    TemplateSection,
)


class CodeSnippetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CodeSnippet

    @factory.sequence
    def slug(n):
        return 'slug_{:02d}'.format(n)


class TemplateFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Template


class TemplateSectionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = TemplateSection

    template = factory.SubFactory(TemplateFactory)
    section = factory.SubFactory(SectionFactory)
