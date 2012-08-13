'''
Created on Aug 12, 2012

@author: e911miri
'''

from google.appengine.api import users

import webapp2
from webapp2_extras.users import login_required

import engine
from models import Message
import cgi

class IndexPage(webapp2.RequestHandler):
    @login_required
    def get(self):
        template_values = engine.globals
        template_values['messages'] = Message.all()
        template = engine.jinja_environment.get_template('messages/index.html')
        self.response.out.write(template.render(template_values))

class InboxPage(webapp2.RequestHandler):
    @login_required
    def get(self):
        template_values = engine.globals
        template_values['messages'] = Message.all()
        template = engine.jinja_environment.get_template('messages/inbox.html')
        self.response.out.write(template.render(template_values))
        
class ComposePage(webapp2.RequestHandler):
    @login_required
    def get(self):
        template_values = engine.globals
        template = engine.jinja_environment.get_template('messages/compose.html')
        self.response.out.write(template.render(template_values))
        
    def post(self):
        recipient = self.request.get("recipient")
        body = self.request.get("body")
        title = self.request.get("title")
        msg = Message(sender=str(engine.globals['user']), recipient=recipient, title=title, body=body)
        msg.put()
        template_values = engine.globals
        template_values['message'] = msg
        template = engine.jinja_environment.get_template('messages/confirm.html')
        self.response.out.write(template.render(template_values))
        
class ShowPage(webapp2.RequestHandler):
    @login_required
    def get(self, key):
        template_values = engine.globals
        template_values['message'] = Message.get(cgi.escape(key))
        template = engine.jinja_environment.get_template('messages/show.html')
        self.response.out.write(template.render(template_values))
        
        
class DraftsPage(webapp2.RequestHandler):
    @login_required
    def get(self):
        template_values = engine.globals
        template = engine.jinja_environment.get_template('compose.html')
        self.response.out.write(template.render(template_values))
        
class SentPage(webapp2.RequestHandler):
    @login_required
    def get(self):
        template_values = engine.globals
        template = engine.jinja_environment.get_template('compose.html')
        self.response.out.write(template.render(template_values))
