# -*- encoding: utf-8 -*-
from django import forms

from base.form_utils import (
    bleach_clean,
    RequiredFieldForm,
)

from .models import (
    Article,
    Feature,
    FeatureStyle,
    Header,
    HeaderStyle,
)


class ArticleEmptyForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ()


class ArticleForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for name in ('title', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    def clean_description(self):
        data = self.cleaned_data['description']
        return bleach_clean(data)

    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            #'picture',
            'article_type',
        )
        #widgets = {
        #    'picture': forms.FileInput,
        #}


class FeatureForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(FeatureForm, self).__init__(*args, **kwargs)
        for name in ('title', 'description'):
            self.fields[name].widget.attrs.update({
                'class': 'pure-input-2-3',
            }),
        self.fields['title'].widget.attrs.update({
            'rows': '1',
        })

    class Meta:
        model = Feature
        fields = (
            'title',
            'description',
            'style',
            'picture',
        )
        widgets = {
            'picture': forms.FileInput,
        }


class FeatureStyleForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(FeatureStyleForm, self).__init__(*args, **kwargs)
        for name in ('name', 'css_class_name'):
            self.fields[name].widget.attrs.update({
                'class': 'pure-input-2-3',
            })

    class Meta:
        model = FeatureStyle
        fields = (
            'name',
            'css_class_name',
        )


class HeaderForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(HeaderForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'pure-input-2-3',
        })
        self.fields['title'].widget.attrs.update({
            'rows': '3',
        })

    def clean_title(self):
        data = self.cleaned_data['title']
        return bleach_clean(data)


    class Meta:
        model = Header
        fields = (
            'title',
            'style',
        )


class HeaderStyleForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(HeaderStyleForm, self).__init__(*args, **kwargs)
        for name in ('name', 'css_class_name'):
            self.fields[name].widget.attrs.update({
                'class': 'pure-input-2-3',
            })

    class Meta:
        model = HeaderStyle
        fields = (
            'name',
            'css_class_name',
        )


