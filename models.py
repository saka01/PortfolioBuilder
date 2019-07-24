from google.appengine.ext import ndb

class ResumeInfo(ndb.Model):
    name= ndb.StringProperty(required=True)
    dob= ndb.StringProperty(required=True)
    address= ndb.StringProperty(required=True)
    education= ndb.StringProperty(required=True)
    work_experience= ndb.StringProperty(required=True)
    bio= ndb.StringProperty(required=True)
    email= ndb.StringProperty(required=True)

    def printResumeInfo(self):
        print(self.Name+ " " + self.DOB + " " + self.Address + " " + self.Education + " " + self.Work_Experience + " " + self.Bio)

class PortfolioUser(ndb.Model):
    email = ndb.StringProperty(required=True)
