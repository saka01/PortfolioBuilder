from google.appengine.ext import ndb

class ResumeInfo(ndb.Model):
    name = ndb.StringProperty(required=True)

class PortfolioUser(ndb.Model):
    email = ndb.StringProperty(required=True)
