'''
Created on Aug 12, 2012

@author: e911miri
'''
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users

import webapp2
import jinja2
import os
import public.views, timetable.views, messages.views
from webapp2_extras import routes


globals = {'user': users.get_current_user(),
         'sign_in': users.create_login_url("/"),
         'sign_out': users.create_logout_url("/")}

base_path = os.path.dirname(__file__)
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/templates"))

app = webapp2.WSGIApplication([('/', public.views.MainPage),
                               routes.PathPrefixRoute('/timetables', [
                                webapp2.Route('/', timetable.views.MainPage),
                                webapp2.Route('/comment', timetable.views.CommentPage),
                                routes.PathPrefixRoute('/timeslot', [
                                 webapp2.Route('/', timetable.views.TimeslotPage),
                                 webapp2.Route('/create', timetable.views.CreatePage)
                                ]),
                               ]),
                               routes.PathPrefixRoute('/messages', [
                                webapp2.Route('/', messages.views.IndexPage),
                                webapp2.Route('/inbox', messages.views.InboxPage),
                                webapp2.Route('/sent', messages.views.SentPage),
                                webapp2.Route('/drafts', messages.views.DraftsPage),
                                webapp2.Route('/compose', messages.views.ComposePage),
                                webapp2.Route('/show/<key:\w+\-\w+>', messages.views.ShowPage),
                               ])
                               ],
                                debug=True)

def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    main()

