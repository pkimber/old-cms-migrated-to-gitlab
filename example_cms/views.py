# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from base.view_utils import BaseMixin
from cms.models import CodeSnippet


class DashView(BaseMixin, TemplateView):

    template_name = 'example/dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dash_css = ''
        try:
            obj = CodeSnippet.objects.get(slug=CodeSnippet.CSS)
            snippet = obj.code
        except CodeSnippet.DoesNotExist:
            snippet = ''
        context.update(dict(snippet=snippet))
        return context


class SettingsView(BaseMixin, TemplateView):

    template_name = 'example/settings.html'
