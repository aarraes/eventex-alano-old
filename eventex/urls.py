from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'eventex.core.views.homepage', name='homepage'),
    url(r'^inscricao/$', 'eventex.subscriptions.views.subscribe', name='subscribe'),
)
