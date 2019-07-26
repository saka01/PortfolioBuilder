from google.appengine.ext import ndb

def resume_info_key(resume_info_name=None):
    """Constructs a Datastore key for a Guestbook entity with name."""
    return ndb.Key('ResumeInfo', resume_info_name or 'default_resume_info')

class ResumeInfo(ndb.Model):
    name= ndb.StringProperty(required=True)
    image = ndb.BlobProperty(required=False)
    current_position= ndb.StringProperty(required=True)
    address= ndb.StringProperty(required=True)
    number= ndb.StringProperty(required=True)
    email= ndb.StringProperty(required=True)
    education= ndb.StringProperty(required=True)
    work_experience= ndb.StringProperty(required=True)
    objective= ndb.StringProperty(required=True)
    email= ndb.StringProperty(required=True)
    institute= ndb.StringProperty(required=True)
    graduation_year= ndb.StringProperty(required=True)
    concentration= ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=True)
    title= ndb.StringProperty(required=True)
    title2= ndb.StringProperty(required=True)
    title3= ndb.StringProperty(required=True)
    title4= ndb.StringProperty(required=True)
    userex1= ndb.StringProperty(required=True)
    userex2= ndb.StringProperty(required=True)
    proj1= ndb.StringProperty(required=True)
    proj2= ndb.StringProperty(required=True)
    user_project= ndb.StringProperty(required=True)
    start= ndb.StringProperty(required=True)
    end= ndb.StringProperty(required=True)
    start2= ndb.StringProperty(required=True)
    end2= ndb.StringProperty(required=True)


    def printResumeInfo(self):
        print(self.Name+ " " + self.CurrentPosition+ " " + self.Address + " " + self.Number + " " + self.Email + " " + self.Objective + " " + self.Location)

class PortfolioUser(ndb.Model):
    email= ndb.StringProperty(required=True)
