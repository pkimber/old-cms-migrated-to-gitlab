# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from .views import (
    DashView,
    SettingsView,
)

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(r'^home/user/$',
        view=DashView.as_view(),
        name='project.dash'
        ),
    url(r'^settings/$',
        view=SettingsView.as_view(),
        name='project.settings'
        ),
    url(regex=r'^cms/',
        view=include('cms.urls.cms')
        ),
    url(regex=r'^compose/',
        view=include('compose.urls')
        ),
    # this url include should come last
    url(regex=r'^',
        view=include('cms.urls.page')
        ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user

urlpatterns += staticfiles_urlpatterns()
