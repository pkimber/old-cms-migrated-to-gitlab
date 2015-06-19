# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    ArticleCreateView,
    ArticlePublishView,
    ArticleRemoveView,
    ArticleUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^article/create/(?P<page>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=ArticleCreateView.as_view(),
        name='compose.article.create'
        ),
    url(regex=r'^article/create/(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=ArticleCreateView.as_view(),
        name='compose.article.create'
        ),
    url(regex=r'^article/(?P<pk>\d+)/publish/$',
        view=ArticlePublishView.as_view(),
        name='compose.article.publish'
        ),
    url(regex=r'^article/(?P<pk>\d+)/remove/$',
        view=ArticleRemoveView.as_view(),
        name='compose.article.remove'
        ),
    url(regex=r'^article/(?P<pk>\d+)/update/$',
        view=ArticleUpdateView.as_view(),
        name='compose.article.update'
        ),
)
