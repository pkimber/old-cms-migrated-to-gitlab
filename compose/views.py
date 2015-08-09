# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from django.views.generic.list import ListView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)
from block.forms import ContentEmptyForm
from block.views import (
    ContentCreateView,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
)

from .forms import (
    ArticleEmptyForm,
    ArticleForm,
    FeatureForm,
    FeatureStyleForm,
    HeaderForm,
    HeaderStyleForm,
)
from .models import (
    Article,
    ArticleBlock,
    Feature,
    FeatureBlock,
    FeatureStyle,
    Header,
    HeaderBlock,
    HeaderStyle,
)


class ArticleCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = ArticleBlock
    form_class = ArticleForm
    model = Article
    template_name = 'compose/article_create.html'


class ArticlePublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Article
    template_name = 'compose/article_publish.html'


class ArticleRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Article
    template_name = 'compose/article_remove.html'


class ArticleUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = ArticleForm
    model = Article
    template_name = 'compose/article_update.html'

class FeatureCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = FeatureBlock
    form_class = FeatureForm
    model = Feature
    template_name = 'compose/feature_create_update.html'


class FeaturePublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Feature
    template_name = 'compose/feature_publish.html'


class FeatureRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Feature
    template_name = 'compose/feature_remove.html'


class FeatureUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = FeatureForm
    model = Feature
    template_name = 'compose/feature_create_update.html'


class FeatureStyleCreateView (LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    form_class = FeatureStyleForm
    model = FeatureStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.feature.style.list')


class FeatureStyleUpdateView (LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    form_class = FeatureStyleForm
    model = FeatureStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.feature.style.list')


class HeaderCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = HeaderBlock
    form_class = HeaderForm
    model = Header
    template_name = 'compose/header_create_update.html'


class HeaderPublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Header
    template_name = 'compose/header_publish.html'


class HeaderUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = HeaderForm
    model = Header
    template_name = 'compose/header_create_update.html'


class HeaderRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Header
    template_name = 'compose/header_remove.html'


class HeaderStyleCreateView (LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    form_class = HeaderStyleForm
    model = HeaderStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.header.style.list')


class HeaderStyleUpdateView (LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    form_class = HeaderStyleForm
    model = HeaderStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.header.style.list')


class FeatureStyleListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = FeatureStyle


class HeaderStyleListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = HeaderStyle


