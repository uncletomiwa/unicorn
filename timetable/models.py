from google.appengine.ext import db
# Create your db here.

class Timeslot(db.Model):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    tfrom = db.IntegerProperty()
    tto = db.IntegerProperty()
    day = db.StringProperty()
    venue= db.StringProperty()
    notes=db.StringProperty()
    course = db.StringProperty()
    def __unicode__(self):
        return "{0}: {1}-{2}, {3} ".format(self.course, self.tfrom, self.tto, self.day)

class Comment(db.Model):
    content = db.TextProperty()
    user = db.UserProperty()
    time = db.TimeProperty(auto_now_add=True)
    timeslot = db.ReferenceProperty(Timeslot)
    def __unicode__(self):
        return self.content

class Person(db.Model):
    username = db.StringProperty()
    picture = db.URLProperty()
    token = db.StringProperty()
    name = db.StringProperty()
    service = db.StringProperty()
    secret = db.StringProperty()

class Student(db.Model):
    person = db.ReferenceProperty(Person)
    level = db.IntegerProperty()
#
#class Assignment(db.Model):
#    course = db.ForeignKey(Course)
#    details = db.TextProperty()
#    date_posted = db.DateProperty()
#    date_expected = db.DateProperty()
#    comment = db.TextProperty()
#    pass
#

#    
#class PastQuestion(db.Model):
#    year = db.IntegerProperty()
#    pass
#
#class People(db.Model):
#    pass
#
#class TimeSlot(db.Model):
#    day= db.CharProperty(max_length=11)
#    tag = db.CharProperty(max_length=20)
#    time_from = db.CharProperty( max_length=11)
#    time_to = db.CharProperty(max_length=11)
#    info = db.TextProperty()
#    pass
#
#
#class Tutorial(db.Model):
#    pass
#
#class ShoutBox(db.Model):
#    pass 
#
#class Venue(db.Model):
#    pass  
