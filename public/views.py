# Create your views here.\
from google.appengine.api import users
import engine
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = engine.globals
        template = engine.jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))



