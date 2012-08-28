'''
Created on Aug 16, 2012

@author: e911miri
'''
from google.appengine.ext import db
class Event(db.Model):
    title=db.StringProperty()
    details=db.TextProperty()
    datetime=db.DateTimeProperty()