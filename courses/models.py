'''
Created on Aug 12, 2012

@author: e911miri
'''
from google.appengine.ext import db


class School(db.Model):
    name = db.StringProperty()

class Department(db.Model):
    name = db.StringProperty()
    school=db.ReferenceProperty(School)

class Course(db.Model):
    code =db.StringProperty()
    unit=db.IntegerProperty()
    level = db.IntegerProperty()
    summary = db.TextProperty()
    title = db.StringProperty()
    synopsis = db.TextProperty()
    department = db.ReferenceProperty(Department)
    def __unicode__(self):
        return self.title