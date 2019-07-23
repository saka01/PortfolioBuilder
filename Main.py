import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

#jijna2.environment is a constructor
jinja_ev = jinja2.Environment(
    # /Users/cssi/Desktop/cssi-labs/python/labs/appengine
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CssiUser(ndb.Model):
    first_name = ndb.StringProperty()
    email = ndb.StringProperty()
    age = ndb.IntegerProperty()


class LoginPage(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            button_dict = {
                "logout" : logout_url
            }
            existing_user = CssiUser.query().filter(CssiUser.email == email_address).get()
            if existing_user:
                home_template = jinja_ev.get_template("Home.html")
                self.response.write(home_template.render())
            else:
                register_template = jinja_ev.get_template("Registeration.html")
                self.response.write(register_template.render(button_dict))


        else:
            login_url = users.create_login_url("/")
            login_button = '<a href="%s"> Sign In</a>' % login_url
            # login_button = '<a href="' + login_url + '"> Sign In</a>'
            self.response.write("Please log in!<br>" + login_button)

def post(Self):
    user = users.get_current_user()

    cssi_user = CssiUSer(
        first_name = self.request.get("first_name"),
        age = int(self.request.get("age")),
        email = user.nickname()
    )
    cssi_user.put()
    self.response.write("thanks for registering")

class HomePage(webapp2.RequestHandler):
    def post(self):
        home_template = jinja_ev.get_template("Home.html")
        self.response.write(home_template.render())


#the app configuration section
app = webapp2.WSGIApplication(
    [
        ("/", LoginPage),
        ("/home", HomePage),

    ], debug = True
)
