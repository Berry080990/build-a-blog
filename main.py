import webapp2
import cgi
import jinja2
import os
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

"""class Blog(db.Blog):
    title = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)"""

class Handler(webapp2.RequestHandler):
    def renderError(self, error_code):
        self.error(error_code)
        self.response.write("Oops! Something went wrong.")

class Index(Handler):
    def get(self):
        t = jinja_env.get_template("newpost.html")
        content = t.render(
            title = ""
            )
        self.response.write(content)

    def post(self):
        title = self.request.get('title')
        body = self.request.get('body')

        if title and body:
            self.response.write("Thanks!")
        else:
            t = jinja_env.get_template("newpost.html")
            content = t.render(
                title = title,
                body = body,
                error = "Please include a title AND body!"
                )
            self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
