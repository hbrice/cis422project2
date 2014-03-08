from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunarshiftsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url(r'^$', views.index, name='index'),
		url(r'^$', include('lunarshiftapp.urls')),
		url(r'^login$', 'lunarshiftapp.views.login_view'),
    url(r'^admin/', include(admin.site.urls)),
)
