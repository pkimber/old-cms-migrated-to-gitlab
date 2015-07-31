# -*- encoding: utf-8 -*-
from django import forms

from base.form_utils import RequiredFieldForm
from block.models import (
    Page,
    Section,
)

from .models import (
    CodeSnippet,
    HeaderFooter,
    Template,
    TemplateSection,
)


class CodeSnippetCreateForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('code',):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = CodeSnippet
        fields = (
            'slug',
            'code',
        )


class CodeSnippetUpdateForm(CodeSnippetCreateForm):

    class Meta:
        model = CodeSnippet
        fields = (
            'code',
        )


class HeaderFooterForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('header', 'url_facebook', 'url_linkedin', 'url_twitter'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = HeaderFooter
        fields = (
            'header',
            'url_facebook',
            'url_linkedin',
            'url_twitter',
        )


class PageEmptyForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ()


class PageForm(RequiredFieldForm):

    template = forms.ModelChoiceField(queryset=Template.objects.all())

    class Meta:
        model = Page
        fields = (
            'name',
            'slug',
            'slug_menu',
            'order',
            'is_home',
            'template',
        )


class SectionForm(RequiredFieldForm):

    class Meta:
        model = Section
        fields = (
            'name',
            'slug',
            'block_app',
            'block_model',
            'create_url_name',
            'paginated',
        )


class TemplateForm(RequiredFieldForm):

    class Meta:
        model = Template
        fields = (
            'template_name',
        )


class TemplateSectionEmptyForm(forms.ModelForm):

    class Meta:
        model = TemplateSection
        fields = ()


class TemplateSectionForm(RequiredFieldForm):

    class Meta:
        model = TemplateSection
        fields = (
            'section',
        )
