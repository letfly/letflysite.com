from django.conf.urls import patterns, include, url
from lsite.view import Index
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'letflysite.views.home', name='home'),
	# url(r'^letflysite/', include('letflysite.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^$', Index.as_view(), name='home'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/',include('lblog.urls')),
	url(r'^captcha/', include('captcha.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns("",
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}
		),
	)
