import os
import webapp2
import jinja2
import logging
import string
import json
import time

from google.appengine.api import rdbms
from google.appengine.ext import webapp
import os
 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
 
from gaesessions import get_current_session

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import memcache
from controllers import *
from settings import common

# Paths and Jinja2
template_path = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_path)
) 
                 
class MainHandler(webapp.RequestHandler):
    def get(self):
        conn = common.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pop.pop_attr") 
        zones = cursor.fetchall()
        conn.close()
        
                # Get the current session        
        session = get_current_session()
 
        # Get the value of the counter,
        # defaulting to 0 if not present
        counter = session.get('counter', 0)
        if zones is '':
            session.set_quick('zones', zones)
        else:
            zones1  = session.get('zones', zones)
        #zones1 = session.pop_quick('zones')
        
 
        # Increment the counter
        session['counter'] =  counter + 1 
 
        context = {
             "counter": counter 
        }
        
        template_values = {'zones1': zones1, 'zones': zones, 'counter': counter }
        template = jinja2_env.get_template('index.html')
        self.response.out.write(template.render(template_values)) 
        
application = webapp.WSGIApplication(
    [
        ('/', MainHandler),

        

    ],
    debug=True
    )