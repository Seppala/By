import requests
import sys
import simplejson
import csv
from django.contrib.auth.models import User
from upfo.jsonhandler.jsonhelpers import *
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

def turn_true(ii):
	try:
		ii.get_profile().is_upfo = True
		return True
	except:
		return False

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
	
	users = User.objects.all()
	social_users = UserSocialAuth.objects.all()
	print('in fau: users:' + str(users))
	print('in fau: social_users:' + str(social_users))
	#for each person in the dict 
	#print(friends_dict['data'])
	for friend in friends_dict['data']:
		#check if they are users
		#print('in for loop')
		#get the facebook id
		ids = friend['id']
		#print('ids:' + str(ids))
		print(social_users.get(uid='48300441'))
		thisguy = social_users.get(uid='48300441')
		print('thisguy.User:' + str(thisguy.get().uid))
		try:
			thisguy = social_users.get(uid=ids)
			#if they are users check if they are upfo
			#if they are, add to an upfo list
			print('got thisguy as existing:' + str(thisguy))
			try:
				thisuser = users.get(Username = thisguy.User)
				if thisguy.get_profile().is_upfo == True:
					print("and he's upfo")
					upfos.append(thisguy)
				#if they're not, add to a user list
				else:
					print("appending to users list")
					users.append(thisguy)
			except: 
				print("couldn't get thisuser profile by Username")
			
			
		except:
			#if the user can't be found in the database, he's a non-user...
			nonusers.append(friend)
			print(' appending to non-user')
	
	user_lists = {'upfos': upfos, 'users': users, 'nonusers': nonusers }
	return user_lists
		
	
	
	