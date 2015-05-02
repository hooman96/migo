from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webmigo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'migoapp.views.index'),
    url(r'^index', 'migoapp.views.index'),
    url(r'^search/(?P<searchterm>\w+)/', 'migoapp.views.spec'), 

)
