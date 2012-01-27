import requests
import sys
import simplejson
import csv
from django.contrib.auth.models import User

def fetch_json_to_dict(url):
	
	#fetch the page defined in the argument url 
    r = requests.get(url)
    # We extract the contents
    c = r.content
    # And load the json into a python dict
    j = simplejson.loads(c)
    
    # And return the dict
    return j

def check_friends_for_users(j):
	#Well save all the friends' names and uid's in a dictionary called dicta
	dicta = {}
	#Just a counter
	i = 0
	#for all id's in j, see if there is corresponding user in the user database.
	for f in j["data"]:
		#for User.objects.all():
			try:
				u = User.objects.get(uid= f['id'])
				# If the user object is found, create a new item in the dicta with id = uidn and name = 
				dicta2 = {'name': f['name'], 'id': f['id'], 'upfo': u.is_upfo}
				dicta[i] = dicta2
				i += 1
			except:
				print('no user with that uid...')
	return dicta
	