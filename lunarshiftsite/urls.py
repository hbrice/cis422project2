from django.conf.urls import patterns, include, url

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
    url(r'^updateslider$', 'lunarshiftapp.views.updateAvailibility'),
    url(r'^addEmployee$', 'lunarshiftapp.views.addEmployee'),
    url(r'^deleteEmployee$', 'lunarshiftapp.views.deleteEmployee'),
    url(r'^deleteDayToCover$', 'lunarshiftapp.views.deleteDayToCover'),
    url(r'^addTime$', 'lunarshiftapp.views.addTime'),
	url(r'^computeSched$', 'lunarshiftapp.views.computeSchedule'),
	
)
