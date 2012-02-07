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
    dict = simplejson.loads(c)
    
    # And return the dict
    return dict