from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

from upfoMain.views import home, done, logout, error, channel, printFriends, friendson


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^logged-in/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^channel/', channel, name='channel'),
	url(r'^print/', printFriends, name='printFriends'),
	url(r'^friends/', friendson, name='friendson'),
    url(r'', include('social_auth.urls')),
)
