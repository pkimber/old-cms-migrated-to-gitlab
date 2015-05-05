# -*- encoding: utf-8 -*-
from django import forms

from base.form_utils import RequiredFieldForm

from .models import Article


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
            import os
            self.fields['picture'].label = 'Picture (currently "{}")'.format(
                os.path.basename(self.instance.picture.file.name)
            )
            # http://stackoverflow.com/a/25631421
            self.fields['picture'].widget.attrs.update(
                {'style': "color:transparent;"}
            )
            self.fields['picture'].widget.attrs.update(
                {'onchange': "this.style.color = 'black';"}
            )




    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            'picture',
        )
        widgets = {
            'picture': forms.FileInput,
        }
