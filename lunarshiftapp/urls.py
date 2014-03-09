from django.conf.urls import patterns, url

from lunarshiftapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', 'auth.views.login_view'),
)
