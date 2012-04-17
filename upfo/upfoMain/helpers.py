from apscheduler.scheduler import Scheduler
from datetime import datetime, timedelta
import requests
import sys
import simplejson
import csv
from django.contrib.auth.models import User
from upfo.jsonhandler.jsonhelpers import *
from facebookapi.fbhelpers import *
from social_auth.models import UserSocialAuth

def get_lists_response(request):
    #get friends
    friends_list = get_friends(request.user)
    
    #Breaks friends list into three: upfo, users, and nonusers"""
    friends_lists = friends_are_users(friends_list)

    upfos = friends_lists['upfos']
    users = friends_lists['users']
    nonusers = friends_lists['nonusers']

    ctx = {'last_login': request.session.get('social_auth_last_login_backend'), 'upfos': upfos, 'users': users, 'nonusers': nonusers}

    return ctx

def check_friends_for_users(friends_list):
    #Well save all the friends' names and uid's in a dictionary called dicta
    dicta = {}
    #Just a counter
    i = 0
    #for all id's in j, see if there is corresponding user in the user database.
    for friend in friends_list["data"]:
        #for User.objects.all():
            try:
                u = User.objects.get(uid= friend['id'])
                # If the user object is found, create a new item in the dicta with id = uidn and name = 
                dicta2 = {'name': friend['name'], 'id': friend['id'], 'upfo': u.get_profile().is_upfo}
                dicta[i] = dicta2
                i += 1
            except:
                pass
    return dicta

#the auto_false method is called automatically from schedule_false, automatically one hour after a user sets his upfo status to true.
def auto_false(request):
    print('running auto_false')
    ii = request.user.get_profile()
    
    print('upfo situation for auto_false:')
    print(ii.is_upfo)
    #if true, turn to false
    if ii.is_upfo == True:
        ii.is_upfo = False
        ii.save()
    else:
        pass
    
#When user clicks the upfo button, this method is called which toggles the upfo status true or false
def turn_true(request):
   
    ii = request.user.get_profile()

    print(ii.is_upfo) #Here it is False
   
    if ii.is_upfo == None or ii.is_upfo == False:
        ii.is_upfo = True
        ii.save()
        #schedule to turn upfo back to false in 1 hour
        schedule_false([request])
    elif ii.is_upfo == True:
        ii.is_upfo = False
        ii.save()
    
def schedule_false(request):
    
    # Start the scheduler
    sched = Scheduler()
    sched.start()
    # Define the time to be in 1 minute
    now = datetime.now()
    mini = timedelta(minutes=5)
    jobi_date = now + mini 
    #schedule the turn_true job with request as a paremeter
    job = sched.add_date_job(auto_false, jobi_date, request)
    
    
#   try:
#       ii.get_profile().is_upfo = True
#       return True
#   except:
#       return False

def toggle_upfo(ii):
    
    if ii.get_profile().is_upfo == True:
        ii.get_profile().is_upfo = False
    else:
        ii.get_profile().is_upfo = True

#creates a dict of users with flags for if they're users and if they are upfo
def friends_are_users(friends_dict):
    
    upfos = []
    users = []
    nonusers = []
    
    all_users = User.objects.all()
    social_users = UserSocialAuth.objects.all()

    for friend in friends_dict['data']:

        ids = friend['id']

        try:
            thisguy = social_users.get(uid=ids)
            
            thisuser = thisguy.user
            
            try:
                if thisuser.get_profile().is_upfo == True:
                    print("and he's upfo")
                    upfos.append(friend)
                #if they're not, add to a user list
                else:
                    print("appending to users list")
                    users.append(friend)
            except: 
                print("couldn't get thisuser profile by Username")
            
        except:
            #if the user can't be found in the database, he's a non-user...
            nonusers.append(friend)
     
    user_lists = {'upfos': upfos, 'users': users, 'nonusers': nonusers }
    return user_lists
        
    
    
    