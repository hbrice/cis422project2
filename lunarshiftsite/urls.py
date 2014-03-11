from django.conf.urls import patterns, include, url

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunarshiftsite.views.home', name='home'),
	# url(r'^$', views.index, name='index'),
		url(r'^$', include('lunarshiftapp.urls')),
		url(r'^login$', 'lunarshiftapp.views.login_view'),
		url(r'^signout$', 'lunarshiftapp.views.signout_view'),
		url(r'^delete$', 'lunarshiftapp.views.delete_view'),
		url(r'^(?P<employee_type>manager|employee)/(?P<username>\w{0,30})/$', 'lunarshiftapp.views.home_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'.*about.html', 'lunarshiftapp.views.about_view'),
    url(r'.*contact.html', 'lunarshiftapp.views.contact_view'),
    url(r'.*submit_Availability', 'lunarshiftapp.views.submitAvailability'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
