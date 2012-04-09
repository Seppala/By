from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
import settings

from upfoMain.views import home, done, logout, error, channel, printFriends, friendson, turn_true, make_upfo, del_upfo, settingpage, legal, about


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
	#url(r'^hide/(\d+)/$', hide, name='hide'),
    url(r'^done/$', done, name='done'),
	url(r'^logged-in/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^channel/', channel, name='channel'),
	url(r'^print/', printFriends, name='printFriends'),
	url(r'^friends/', friendson, name='friendson'),
    url(r'', include('social_auth.urls')),
	url(r'^make_upfo/$', make_upfo, name='make_upfo'),
	url(r'^del_upfo/$', del_upfo, name='del_upfo'),
	url(r'^settings/$', settingpage, name='settingpage'),
	url(r'^legal/$', legal, name='legal'),
	url(r'^about/$', about, name='about'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': settings.STATIC_URL}),
	#{'document_root': '/Users/rvrseppala/Development/Byy/by/upfo/media'}),
	
)
