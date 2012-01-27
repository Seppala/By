from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.messages.api import get_messages
import requests
from django.utils import simplejson
from helpers import *

from social_auth import __version__ as version

def channel(request):
    
    return render_to_response('channel.html', RequestContext(request))
    
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('home.html', {'version': version},
                                  RequestContext(request))
@login_required
def turn_true(request):
	upfo_updated = turn_true(request.user)
	
	ctx = {'version': version, 'last_login': request.session.get('social_auth_last_login_backend')}
	return render_to_response('done.html', ctx, {'upfo_updated': upfo_updated }, RequestContext(request))
	

@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {'version': version,
           'last_login': request.session.get('social_auth_last_login_backend')}
    return render_to_response('done.html', ctx, RequestContext(request))

def error(request):
    """Error view"""
    messages = get_messages(request)
    return render_to_response('error.html', {'version': version,
                                             'messages': messages},
                              RequestContext(request))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def printFriends(request):
    r = requests.get('http://api.crunchbase.com/v/1/company/facebook.js')
    #r = requests.get('https://graph.facebook.com/me/friends?access_token=AAACEdEose0cBADZA0Q5ZA19IOLJKgwhQVln0RKdOFUCfMb14BMh4kCUwMx36ERWW6IwlxrIExH1mnkZCufvjv2agYNtZBg0KuzQLZB8ZCMOAZDZD')
    c = r.content
    j = simplejson.loads(c)
    
    return render_to_response(j, RequestContext(request))
    #for item in j: 
    #   print item['name']
    #return HttpResponseRedirect('/')

def friendson(request):
	return render_to_response('friends2.js', {'version': version},
                              RequestContext(request))
