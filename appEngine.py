
import webapp2
from google.appengine.ext import ndb

class User(ndb.Model):
    userName = ndb.StringProperty(required=True)
    userDOB= ndb.StringProperty(required=True)
    userAddress= ndb.StringProperty(required=True)
    userEmail= ndb.StringProperty(required=True)

    def printUserInfo(self):
        print(self.userName + " " + self.userDOB + " " + self.userAddress + " " + self.userEmail)
class LoginPage(webapp2.RequestHandler):
    def get(self):
        user1= User(userName= "Smalley", userDOB= "June fifth", userAddress= "0000 Freeland", userEmail= "Smalley2001@gmail.com")
        user1.printUserInfo()
        user1.put()


app = webapp2.WSGIApplication(
    [
        ("/", LoginPage),

    ], debug = True
)
