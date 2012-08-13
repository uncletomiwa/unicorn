# Create your views here.\


import webapp2, engine
from webapp2_extras.users import login_required, admin_required

from timetable.models import Timeslot, Comment
from courses.models import Course

class day:    
    def __init__(self, day):
        self.day = day
        self.timeslots = Timeslot.all().filter("day =", day) 

            
class MainPage(webapp2.RequestHandler):    
    def get(self):        
        days = [day(x) for x in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]]
        template_values = engine.globals
        template_values['days'] = days
        template = engine.jinja_environment.get_template('timetables/index.html')
        self.response.out.write(template.render(template_values))

class CreatePage(webapp2.RequestHandler):
    @admin_required
    def get(self):
        template_values = engine.globals
        template = engine.jinja_environment.get_template('timetables/create.html')
        self.response.out.write(template.render(template_values))
        
    def post(self):
        tfrom = self.request.get("tfrom")
        tto = self.request.get("tto")
        day = self.request.get("day")
        venue = self.request.get("venue")
        course = self.request.get("course")
        notes = self.request.get("notes")
        msg = Timeslot(tfrom=tfrom, tto=tto, day=day, venue=venue, notes=notes, course=Course.get("code=", course))
        msg.put()
        template_values = engine.globals
        template_values['message'] = msg
        template = engine.jinja_environment.get_template('messages/confirm.html')
        self.response.out.write(template.render(template_values))


class TimeslotPage(webapp2.RequestHandler):    
    def get(self):
        key = self.request.get('key')
        if key:
            timeslot = Timeslot.get(key)
            if timeslot:
                template = engine.jinja_environment.get_template('timetables/timeslot.html')
                template_values = engine.globals
                template_values["timeslot"] = timeslot
                template_values["comments"] = Comment.all().filter('timeslot =', timeslot)
                self.response.out.write(template.render(template_values)) 
                
            else:
                print dir(self.request)

class CommentPage(webapp2.RequestHandler):
    def post(self):
        content = self.request.post("content")
        key = self.request.post("key")
        if content and key:
            comment = Comment(content=content, timeslot=Timeslot.get(key))
            comment.put()
        self.redirect(self.request.path)

