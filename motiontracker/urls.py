from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from motiontracker.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'motiontracker.views.home', name='home'),
    # url(r'^motiontracker/', include('motiontracker.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', direct_to_template, {'template': 'index.html'}, name='home'),
    url(r'^track/(?P<track>(.)+)', trackmotion, name='trackmotion'),

)

# debug static serving
if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
			'show_indexes': True
		}),
	)
	urlpatterns+= staticfiles_urlpatterns()
