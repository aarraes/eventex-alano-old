from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'homepage', name='home'),
)
from django.conf import settings
urlpatterns += patterns('django.views.static',
    url(r'^static/(?P<path>.*)$', 'serve',
        {'document_root': settings.STATIC_ROOT}),
)
