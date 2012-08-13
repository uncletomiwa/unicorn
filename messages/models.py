'''
Created on Aug 12, 2012

@author: e911miri
'''
from google.appengine.ext import db
class Message(db.Model):
    sender=db.StringProperty()
    recipient=db.StringProperty()
    title=db.StringProperty()
    body=db.TextProperty()
    status=db.StringProperty()