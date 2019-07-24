import webapp2
import jinja2
import os
from google.appengine.api import users
from models import PortfolioUser
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
                "logout" : logout_url,
            }
            existing_user = PortfolioUser.query().filter(PortfolioUser.email == email_address).get()
            if existing_user:

                print("user is already registered")
                home_template = jinja_ev.get_template("Home.html")
                self.response.write(home_template.render(button_dict))
            else:
                print("user is not registered")
                register_template = jinja_ev.get_template("Registeration.html")
                self.response.write(register_template.render(button_dict))
        else:
            login_url = users.create_login_url("/")
            login_template = jinja_ev.get_template("Login.html")
            button_dict = {
                "login" : login_url
            }
            self.response.write(login_template.render(button_dict))


    def post(self):
        user = users.get_current_user()
        portfolio_user = PortfolioUser(
            email = user.nickname(),
        )
        portfolio_user.put()



class RegisterationPage(webapp2.RequestHandler):
    def post(self):
        logout_url = users.create_logout_url('/')
        button_dict = {
            "logout" : logout_url
        }
        register_template = jinja_ev.get_template("Registeration.html")
        self.response.write(register_template.render(button_dict))

    def get(self):
        user = users.get_current_user()
        portfolio_user = PortfolioUser(
            email = user.nickname(),
        )
        portfolio_user.put()

class HomePage(webapp2.RequestHandler):
    def get(self):
        logout_url = users.create_logout_url('/')
        button_dict = {
            "logout" : logout_url
        }
        home_template = jinja_ev.get_template("Home.html")
        self.response.write(home_template.render(button_dict))

class ResultPage(webapp2.RequestHandler):
    def post(self):
        name= self.request.get("user_name")
        dob = self.request.get("user_DOB")
        add = self.request.get("user_address")
        email= self.request.get("user_email")
        education= self.request.get("user_education")
        userDetails = {
            "DOB": dob,
            "ADDRESS": add,
            "NAME": name,
            "EMAIL": email,
            "EDUCATION": education

        }
        result_template = jinja_ev.get_template("Result.html")
        self.response.write(result_template.render(userDetails))



#the app configuration section
app = webapp2.WSGIApplication(
    [
        ("/", LoginPage),
        ("/home", HomePage),
        ("/registration", RegisterationPage),
        ("/result", ResultPage),

    ], debug = True
)
