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

            print "*"*100
            print email_address

            button_dict = {
                "logout" : logout_url,
            }

            # print("**********************************")
            # print("current logged in email is: " + email_address)


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



class RegisterationPage(webapp2.RequestHandler):
    def post(self):
        print("user registering")
        logout_url = users.create_logout_url('/')
        button_dict = {
            "logout" : logout_url
        }
        register_template = jinja_ev.get_template("Registeration.html")
        self.response.write(register_template.render(button_dict))


class HomePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        email_address = user.nickname()
        print("**********************************")
        print("current logged in email is: " + email_address)
        button_dict = {
            "logout" : logout_url,
        }
        home_template = jinja_ev.get_template("Home.html")
        self.response.write(home_template.render(button_dict))

    # def get(self):
    #     user = users.get_current_user()
    #     email_address = user.nickname()
    #     existing_user = PortfolioUser.query().filter(PortfolioUser.email == email_address).get()
    #     if existing_user:
    #         print("i need to get id now")
    #         ident = resumeInfo.id()

class ResultPage(webapp2.RequestHandler):
    def post(self):
        name= self.request.get("user_name")
        current_position= self.request.get('user_position')
        address = self.request.get("user_address")
        number= self.request.get('user_number')
        email= self.request.get("user_email")
        education= self.request.get("user_education")
        experience = self.request.get('user_experience')
        objective= self.request.get('user_objective')
        institute= self.request.get('institute')
        education= self.request.get('education')
        graduation_year= self.request.get('graduation')
        concentration= self.request.get('concentration')
        location=self.request.get('location')
        title=self.request.get('title')
        title2= self.request.get('title2')
        title3= self.request.get('title3')
        title4= self.request.get('title4')
        userex1= self.request.get('userex1')
        userex2= self.request.get('userex2')
        proj1= self.request.get('proj1')
        proj2= self.request.get('proj2')
        user_project= self.request.get('user_project')
        start= self.request.get('start')
        end= self.request.get('end')
        start2= self.request.get('start2')
        end2= self.request.get('end2')
        print('title'+ title)

        resumeInfo= ResumeInfo(name=name,
            current_position=current_position,
            address=address,
            number=number,
            email=email,
            education=education,
            work_experience=experience,
            objective=objective,
            institute=institute,
            graduation_year=graduation_year,
            location=location,
            concentration=concentration,
            title=title,
            title2=title2,
            title3=title3,
            title4=title4,
            userex1=userex1,
            userex2=userex2,
            proj1=proj1,
            proj2=proj2,
            user_project=user_project,
            start=start,
            end=end,
            start2=start2,
            end2=end2,
            )
        # print('resumeInfo'+str(resumeInfo))
        userDetails = {
            "NAME" : name,
            "CURRENTPOSITION" : current_position,
            "ADDRESS" : address,
            "PNUMBER": number,
            "EMAIL": email,
            "EDUCATION": education,
            "EXPERIENCE": experience,
            "OBJECTIVE": objective,
            "INSTITUTE": institute,
            "GRADUATION_YEAR": graduation_year,
            "CONCENTRATION": concentration,
            "LOCATION": location,
            "TITLE":title,
            "TITLE2":title2,
            "TITLE3": title3,
            "TITLE4":title4,
            "USEREX1": userex1,
            "USEREX2": userex2,
            "PROJ1": proj1,
            "PROJ2":proj2,
            "PROJECT": user_project,
            "START": start,
            "END":end,
            "START2": start2,
            "END2": end2,

        }
        result_template = jinja_ev.get_template("Result.html")
        self.response.write(result_template.render(userDetails))

        user = users.get_current_user()
        portfolio_user = PortfolioUser(
        email = user.nickname(),
        )
        portfolio_user.put()
        resumeInfo.put()
        #
        # resumeprint = resumeInfo.put()
        # print(resumeprint)
        #
        # mu = resumeInfo(id = users.get_current_user().id())
        # mu.put()


#the app configuration section
app = webapp2.WSGIApplication(
    [
        ("/", LoginPage),
        ("/home", HomePage),
        ("/registration", RegisterationPage),
        ("/result", ResultPage),

    ], debug = True
)
