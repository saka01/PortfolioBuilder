from google.appengine.ext import ndb

class ResumeInfo(ndb.Model):
    name = ndb.StringProperty(required=True)
    
