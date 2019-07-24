from google.appengine.ext import ndb

class ResumeInfo(ndb.Model):
    name= ndb.StringProperty(required=True)
    current_position= ndb.StringProperty(required=True)
    address= ndb.StringProperty(required=True)
    number= ndb.StringProperty(required=True)
    email= ndb.StringProperty(required=True)
    education= ndb.StringProperty(required=True)
    work_experience= ndb.StringProperty(required=True)
    bio= ndb.StringProperty(required=True)
    email= ndb.StringProperty(required=True)

    def printResumeInfo(self):
        print(self.Name+ " " + self.CurrentPosition+ " " + self.Address + " " + self.Number + " " + self.Email + " " + self.Bio)

class PortfolioUser(ndb.Model):
    email = ndb.StringProperty(required=True)
