import webapp2
import jinja2
import os
from google.appengine.api import users
from models import PortfolioUser
from models import ResumeInfo
#jijna2.environment is a constructor
jinja_ev = jinja2.Environment(
    # /Users/cssi/Desktop/cssi-labs/python/labs/appengine
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class LoginPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        print("On login page")
        if user:
            print("user is logged in to gmail")
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            button_dict = {
                "logout" : logout_url
            }
            existing_user = PortfolioUser.query().filter(PortfolioUser.email == email_address).get()
            if existing_user:
                print("user is already registered")
                home_template = jinja_ev.get_template("Home.html")
                self.response.write(home_template.render())
            else:
                print("user is not registered")
                register_template = jinja_ev.get_template("Registeration.html")
                self.response.write(register_template.render(button_dict))
        else:
            login_url = users.create_login_url("/")
            login_button = '<a href="%s"> Sign In</a>' % login_url
            # login_button = '<a href="' + login_url + '"> Sign In</a>'
            self.response.write("Please log in!<br>" + login_button)

    def post(self):
        user = users.get_current_user()
        portfolio_user = PortfolioUser(
            email = user.nickname(),
        )
        portfolio_user.put()

class HomePage(webapp2.RequestHandler):
    def post(self):
        home_template = jinja_ev.get_template("Home.html")
        self.response.write(home_template.render())

class ResultPage(webapp2.RequestHandler):
    def post(self):
        userName= self.request.get('user_name')
        userDob= self.request.get('user_dob')
        userAddress= self.request.get('user_address')
        userMail= self.request.get('user_mail')
        userEd= self.request.get('user_education')
        userEx= self.request.get('user_experience')
        userBio= self.request.get('user_bio')
        resumeInfo= ResumeInfo(name=userName,dob=userDob,address=userAddress,email=userMail,education=userEd,work_experience=userEx,bio=userBio)
        result_template = jinja_ev.get_template("Result.html")
        self.response.write(result_template.render())

        resumeInfo.put()



#the app configuration section
app = webapp2.WSGIApplication(
    [
        ("/", LoginPage),
        ("/home", HomePage),
        ("/result", ResultPage),

    ], debug = True
)
