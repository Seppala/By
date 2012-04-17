from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import threading
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.messages.api import get_messages
import requests
from django.utils import simplejson
from helpers import *
from facebookapi.fbhelpers import *
from social_auth import __version__ as version

def channel(request):
    
    return render_to_response('channel.html', RequestContext(request))
    
@csrf_exempt
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('home.html', {'version': version},
                                  RequestContext(request))
#adds a user to the hidden user list 
#@login_required
#def hide(request, id):
    #add id to hidden user list
 #   u = request.user
  #  ii = u.get_profile()

@login_required
def settingpage(request):
	
	return render_to_response('settings.html', RequestContext(request))
	
def legal(request):

	return render_to_response('legal.html', RequestContext(request))
	
def about(request):

	return render_to_response('about.html', RequestContext(request))


@login_required
@csrf_exempt
def make_upfo(request):
    
    profile = request.user.get_profile()
    
    if profile.is_upfo == True:
        pass
    else:
        turn_true(request)
    
    response = get_lists_response(request)
    
    return render_to_response('is_upfo.html', response, RequestContext(request))

@csrf_exempt
def facebook(request):
	return render_to_response('facebook.html', RequestContext(request))

@login_required
@csrf_exempt
def del_upfo(request):
    
    profile = request.user.get_profile()
    
    if profile.is_upfo == False or profile.is_upfo == None:
        pass
    else:
        turn_true(request)

    return render_to_response('not_upfo.html', RequestContext(request))

@login_required
@csrf_exempt
def list_page(request):
    #Turn upfo true or false
    turn_true(request)
    
    #if upfo is true, set timer to turn upfo to false
    ii = request.user
    prof = ii.get_profile()
    
    #if prof.is_upfo is True:
     #   t = threading.Timer(30.0, turn_true(request))
      #  t.start() # after 30 seconds, "hello, world" will be printed
    #else:
     #   pass
    
    friends_list = get_friends(request.user)
    """Breaks friends list into three: upfo, users, and nonusers"""
    friends_lists = friends_are_users(friends_list)

    upfos = friends_lists['upfos']
    users = friends_lists['users']
    nonusers = friends_lists['nonusers']

    ctx = {'version': version,
       'last_login': request.session.get('social_auth_last_login_backend'), 'upfos': upfos, 'users': users, 'nonusers': nonusers}
    return render_to_response('is_upfo.html', ctx, RequestContext(request))

    #except:
     #   return render_to_response('turn.html', RequestContext(request))

@login_required
@csrf_exempt
def done(request):
    #get profile so that you can check if the user is upfo
    profile = request.user.get_profile()
    
    #if user is upfo get the lists of friends and show the is_upfo page
    if profile.is_upfo == True:
        #gets lists of friends
        response = get_lists_response(request)
        
        return render_to_response('is_upfo.html', response, RequestContext(request))
    #if the user isn't upfo show the not_upfo page
    else:
        return render_to_response('not_upfo.html', RequestContext(request))
        
    #try:
     #   friends_list = get_friends(request.user)
        #"""Breaks friends list into three: upfo, users, and nonusers"""
      #  friends_lists = friends_are_users(friends_list)
        #print(friends_lists)
       # upfos = friends_lists['upfos']
        #users = friends_lists['users']
        #nonusers = friends_lists['nonusers']        
    
        #ctx = {'version': version,
         #   'last_login': request.session.get('social_auth_last_login_backend'), 'upfos': upfos, 'users': users, 'nonusers': nonusers}
        #return render_to_response('done.html', ctx, RequestContext(request))
    #except:
     #   messages = get_messages(request)
      #  return render_to_response('done.html', {'messages': messages}, RequestContext(request))

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
