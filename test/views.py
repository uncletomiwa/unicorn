'''
Created on Aug 16, 2012

@author: e911miri
'''
import webapp2
from events.models import Event
import datetime
class IndexPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Creating New Event")
        e=Event(title="GDG Meetup", details="Final Google Technology User group Hackup Meetup",
                 datetime=datetime.datetime.today())
        self.response.out.write("Begin Saving New Event")
        e.put()
        self.response.out.write("Complete Saving New Event")
        pass