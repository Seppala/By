# Define a custom User class to work with django-social-auth
from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_upfo = models.NullBooleanField(null=True, default=False)
    #hiddens = models.TextField(blank=True, null=True)
    
    #is_active  = BooleanField()
    #friends = models.ManyToManyField("Friends")

    def is_authenticated(self):
        return True

from social_auth.signals import pre_update, socialauth_registered
from social_auth.backends.facebook import FacebookBackend

#extend new user at creation
def new_users_handler(sender, user, response, details, **kwargs):
    user.is_new = True
    profile = CustomUser(user=user)
    if user.is_new:
        profile.is_upfo = False
        profile.save()

socialauth_registered.connect(new_users_handler, sender=None)   

def facebook_extra_values(sender, user, response, details, **kwargs):
    return False

pre_update.connect(facebook_extra_values, sender=FacebookBackend)
