import webapp2
import jinja2
import os
from google.appengine.api import users
from models import PortfolioUser
from google.appengine.api import images
from models import ResumeInfo
import models
from google.appengine.ext import ndb
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
            resume_check = ResumeInfo.query().filter(ResumeInfo.loginemail == email_address).fetch()
            ids = []
            for r in resume_check:
                print(r.key.id())
                ids.append(r.key.id())


            resume = None
            id = self.request.get('id')
            if id != None and id != "":
                print("resume id found")
                resumes = ResumeInfo.query().fetch()
                for r in resumes:
                    if r.key.id() == int(id):
                        print("resume found")
                        resume = r
                        break


            button_dict = {
                "logout" : logout_url,
                "resumeget" : ids,
                "resume" : resume,
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
        keys = []
        resume_check = ResumeInfo.query().filter(ResumeInfo.loginemail == email_address).fetch()
        for r in resume_check:
            keys.append(r.key.id())
        button_dict = {
            "logout" : logout_url,
            "resumeget" : keys,
            "resume" : None,
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
    def get(self):
        id = long(self.request.get('id'))
        resumes = ResumeInfo.query().fetch()
        resume = None

        for r in resumes:
            if r.key.id() == id:
                print("found it")
                resume = r
                break

        userDetails = {
            "NAME" : resume.name,
            "CURRENTPOSITION" : resume.current_position,
            "ADDRESS" : resume.address,
            "PNUMBER": resume.number,
            "EMAIL": resume.email,
            "IMAGE_ID" : resume.key.urlsafe(),
            "EDUCATION": resume.education,
            "EXPERIENCE": resume.work_experience,
            "OBJECTIVE": resume.objective,
            "INSTITUTE": resume.institute,
            "GRADUATION_YEAR": resume.graduation_year,
            "CONCENTRATION": resume.concentration,
            "LOCATION": resume.location,
            "TITLE": resume.title,
            "TITLE2": resume.title2,
            "TITLE3": resume.title3,
            "TITLE4": resume.title4,
            "USEREX1": resume.userex1,
            "USEREX2": resume.userex2,
            "PROJ1": resume.proj1,
            "PROJ2": resume.proj2,
            "PROJECT": resume.user_project,
            "START": resume.start,
            "END": resume.end,
            "START2": resume.start2,
            "END2": resume.end2,
            "ID" : resume.key.id(),

        }

        result_template = jinja_ev.get_template("Result.html")
        self.response.write(result_template.render(userDetails))

    def post(self):
        user = users.get_current_user()
        loginemail= user.nickname()
        name= self.request.get("user_name")
        image = self.request.get("pic")
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

        image = images.resize(image, 128, 128)
        resumeInfo= ResumeInfo(
            parent=models.resume_info_key(name),
            name=name,
            loginemail=loginemail,
            image=image,
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

        resumeInfo.put()
        # print('resumeInfo'+str(resumeInfo))
        userDetails = {
            "NAME" : name,
            "IMAGE_ID" : resumeInfo.key.urlsafe(),
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

    # def get(self):
    #     id = self.request.get("id")
    #     r = resumeInfo.query().filter(ResumeInfo.key==id).get()
    #     print(r)

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        resume_info_key = ndb.Key(urlsafe=self.request.get('img_id'))

        resume_info = resume_info_key.get()
        if resume_info.image:
            self.response.headers['Content-Type'] = 'image/*'
            self.response.out.write(resume_info.image)
        else:
            self.response.out.write('No image')

#the app configuration section
app = webapp2.WSGIApplication(
    [
        ("/", LoginPage),
        ("/home", HomePage),
        ("/imgs/", ImageHandler),
        ("/registration", RegisterationPage),
        ("/result", ResultPage),

    ], debug = True
)
