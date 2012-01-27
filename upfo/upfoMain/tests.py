"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from upfoMain.helpers import *
from django.contrib.auth.models import User
from django.test import TestCase

class jsonTest(TestCase):
	def test_fetch_json_put_in_dict(self):
		
		url = "http://127.0.0.1:8000/friends"
		#url = "http://api.crunchbase.com/v/1/company/spotify.js"
		
		#just fetch the json to a dict
		j = fetch_json_to_dict(url)
		print('fetched json to dict in  test_fetch_json_put_in_dict...')
		#check that some of the info matches
		
		self.assertEquals(j["data"][0]["name"], "Chris Dotson")
		print('First assert')
		self.assertEquals(j["data"][2]["name"], "Walter Masalin")
		print(j)
		
		#Check that the id for Benjamin Von Kraemer is correct
		for f in j["data"]:
			print(f["name"])
			if f["name"] == "Benjamin Von Kraemer":
				idn = f["id"]
				break
		print('Benkos id is: ' + idn)
		self.assertEquals(idn, '527169848')
		
	def test_are_friends_users(self):
		
		url = "http://127.0.0.1:8000/friends"
		#url = "http://api.crunchbase.com/v/1/company/spotify.js"
		
		#just fetch the json to a dict
		j = fetch_json_to_dict(url)
		print('fetched json to dict in test_are_friends_users...')
		
		dicta = check_friends_for_users(j)
		
		print(dicta)
	
	def test_get_profile(self):
		me = user.get_profile()
		print('my status is:')
		print (me.is_upfo)
		
		
		
		
		
		
		
		
		 
