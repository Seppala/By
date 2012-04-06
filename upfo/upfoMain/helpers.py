from apscheduler.scheduler import Scheduler
from datetime import date
import requests
import sys
import simplejson
import csv
from django.contrib.auth.models import User
from upfo.jsonhandler.jsonhelpers import *
from facebookapi.fbhelpers import *
from social_auth.models import UserSocialAuth


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

def turn_true(request):
    print(' in turn_true')
    friends_list = get_friends(request.user)
    user = request.user
    #print(request.user)
    profile = request.user.get_profile()
    #print(profile)
    ii = request.user.get_profile()
    print('Im in turn true!')
    #print(friends_list)

    print(ii.is_upfo) #Here it is False
    #ii.is_upfo = True
    print(request.user.get_profile().is_upfo) #Does actually change to True
    if ii.is_upfo == None or ii.is_upfo == False:
        ii.is_upfo = True
        print('made it true..')
        ii.save()
    elif ii.is_upfo == True:
        print('so now it comes here...')
        ii.is_upfo = False
        ii.save()
    
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
    print('in fau: users:' + str(all_users))
    print('in fau: social_users:' + str(social_users))
    print('friends dict data:' + str(friends_dict['data']))
    #for each person in the dict 
    #print(friends_dict['data'])
    for friend in friends_dict['data']:
        #check if they are users
        #print('in for loop')
        #get the facebook id]
        ids = friend['id']
        print('this id' + str(ids))
        try:
            thisguy = social_users.get(uid=ids)
            print('this guy:')
            print(thisguy)
            print('this guy User:')
            print(thisguy.user)
            thisuser = thisguy.user
            #print(social_users.get.all())
            #if they are users check if they are upfo
            #if they are, add to an upfo list
            print('got thisguy as existing:' + str(social_users.get(uid=ids)))
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
            print(' appending to non-user now')
    print('nonusers: ')
    print(nonusers)
    print('users: ')
    print(users)
    print('upfos: ')
    print(upfos)
    user_lists = {'upfos': upfos, 'users': users, 'nonusers': nonusers }
    return user_lists
        
    
    
    