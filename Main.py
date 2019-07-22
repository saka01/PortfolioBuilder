import webapp2
import jinja2
import os

#jijna2.environment is a constructor
jinja_ev = jinja2.Environment(
    # /Users/cssi/Desktop/cssi-labs/python/labs/appengine
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = jinja_ev.get_template("Login.html")
        self.response.write(login_template.render())

#the app configuration section
app = webapp2.WSGIApplication(
    [
        ("/", LoginPage),

    ], debug = True
)
