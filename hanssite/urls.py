from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hanssite.views.home', name='home'),
    # url(r'^hanssite/', include('hanssite.foo.urls')),
    url(r'^$', views.HomeView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

