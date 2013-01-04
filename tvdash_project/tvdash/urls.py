from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tvdash.views',
    url('^$', 'index', name='index'),
    url('^search/', 'search', name='search'),
)
