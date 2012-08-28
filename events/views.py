'''
Created on Aug 12, 2012

@author: e911miri
'''
import webapp2
import engine
from events.models import Event
import cgi
class IndexPage(webapp2.RequestHandler):
    def get(self):
        template_values = engine.globals
        template_values['events'] = Event.all()
        template = engine.jinja_environment.get_template('events/index.html')
        self.response.out.write(template.render(template_values))
        
class ShowPage(webapp2.RequestHandler):
    def get(self, key):
        template_values = engine.globals
        template_values['event'] = Event.get(cgi.escape(key))
        template = engine.jinja_environment.get_template('events/show.html')
        self.response.out.write(template.render(template_values))