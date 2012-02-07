"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from upfoMain.helpers import *
from upfo.jsonhandler.jsonhelpers import *
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

class funcTest(TestCase):
    
    # Tests toggling is_upfo
    def test_toggle(self):
        ii = User()
        
        ii.provider = 'Facebook'
        ii.uid = '001'
        
        ii.save()
        
        print(ii.provider)
        
        ii.get_profile().is_upfo = False
        
        toggle_upfo(ii)
        
        self.assertEquals(ii.get_profile().is_upfo, True)

class fbtests(TestCase):
    
    #Setup six test users, three that have installed the app and three that haven't. Make on of them friends with everyone.
    def setUp(self):
    
        i=0

        #create dict for users that have installed by
        users_y = {}

        #create dict for users that haven't installed by
        users_n = {}

        #Create three test users that have the app and three that don't using the fbtestusers app
        while i<3:
            name = 'by' + str(i)
            #create a user that has installed and save to created_y
            created_y = fb_user_create_installed(APP_ID, access_token, name)

            #save in the dict
            users_y[name] = created_y

            name_un = 'byu' + str(i)
            #create a user that has not installed
            created_n = fb_user_create(APP_ID, access_token, name)

            users_n[name_un] = created_n

            #get the users to objects
            by0 = users_y['by0']
            by1 = users_y['by1']
            by2 = users_y['by2']

            byu0 = users_n['byu0']
            byu1 = users_n['byu1']
            byu2 = users_n['byu2']

            #make by0 friends with everyone
            #1. send friend requests
            make_friends(by0, by1)
            make_friends(by0, by2)
            make_friends(by0, byu0)
            make_friends(by0, byu1)
            make_friends(by0, byu2)

        
        
        
        
         
