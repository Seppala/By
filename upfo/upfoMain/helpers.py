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
                print('no user with that uid...')
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
    print('Im in turn true!')
    #print(friends_list)

    print(ii.is_upfo) #Here it is False
   
    if ii.is_upfo == None or ii.is_upfo == False:
        ii.is_upfo = True
        print('made it true..')
        ii.save()
        #schedule to turn upfo back to false in 1 hour
        schedule_false([request])
    elif ii.is_upfo == True:
        print('so now it comes here...')
        ii.is_upfo = False
        ii.save()
    
def schedule_false(request):
    
    # Start the scheduler
    print('doing the scheduling..')
    sched = Scheduler()
    sched.start()
    # Define the time to be in 1 minute
    now = datetime.now()
    mini = timedelta(minutes=1)
    jobi_date = now + mini 
    print('current time is: ')
    print(now)
    print('jobi_date is: ')
    print(jobi_date)
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
    #print('in fau: users:' + str(all_users))
    #print('in fau: social_users:' + str(social_users))
    #print('friends dict data:' + str(friends_dict['data']))
    #for each person in the dict 
    #print(friends_dict['data'])
    for friend in friends_dict['data']:
        #check if they are users
        #print('in for loop')
        #get the facebook id]
        ids = friend['id']
        #print('this id' + str(ids))
        try:
            thisguy = social_users.get(uid=ids)
            #print('this guy:')
            #print(thisguy)
            #print('this guy User:')
            #print(thisguy.user)
            thisuser = thisguy.user
            #print(social_users.get.all())
            #if they are users check if they are upfo
            #if they are, add to an upfo list
            #print('got thisguy as existing:' + str(social_users.get(uid=ids)))
            #print('upfo status: ' + str(.get_profile().is_upfo))
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
            #print(' appending to non-user now')
    #print('nonusers: ')
    #print(nonusers)
    #print('users: ')
    #print(users)
    #print('upfos: ')
    #print(upfos)
    user_lists = {'upfos': upfos, 'users': users, 'nonusers': nonusers }
    return user_lists
        
    
    
    