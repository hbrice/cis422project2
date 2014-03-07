from django.conf.urls import patterns, include, url

from django.contrib import admin


import os
admin.autodiscover()


print os.getcwd()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunarshiftsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
