from django.contrib.auth.models import User
from jsonhandler.jsonhelpers import *

#fetch a dict of the users friends (name + uid)
def get_friends(user):

	#get users uid
	print(user.social_auth.get().extra_data)
	dict = user.social_auth.get().extra_data
	access_token = dict['access_token']
	print(access_token)
	#create url for fetching the friends list
	url = 'https://graph.facebook.com/me/friends?access_token=' + access_token

	#use the jsonhelpers to fetch the json to a dict by url
	friends_list = fetch_json_to_dict(url)
	#print(friends_list)
	
	return friends_list