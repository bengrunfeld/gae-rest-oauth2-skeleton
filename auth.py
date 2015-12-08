"""
Retrieve an access token for a Github User

Use the Google Flow workflow to walk through each stage of the OAuth 2.0
process.
"""

import json
import sys
import webapp2

from urlparse import urlparse
from urlparse import parse_qs

from google.appengine.api import urlfetch
from google.appengine.api import users

sys.path.append("lib")

from basehandler import BaseHandler
from config import config


class ShowFrontEnd(BaseHandler):
    """Show the user the UI"""

    def get(self):

        context = {
            "username": 'Ben',
        }

        # Tell user that the app is activated
        self.render('index', context)


config = config()

app = webapp2.WSGIApplication([
    ('/', ShowFrontEnd),
], config=config, debug=True)
