"""
Retrieve an access token for a Github User

Use the Google Flow workflow to walk through each stage of the OAuth 2.0
process.
"""

import sys
import webapp2

from urlparse import urlparse
from urlparse import parse_qs

from google.appengine.ext import db
from google.appengine.api import users

sys.path.append("lib")

import httplib2

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.appengine import CredentialsProperty
from oauth2client.appengine import StorageByKeyName

from model import CredentialsModel 


def create_flow_object():
    """Check if client_secrets.json is populated"""

    # Enter your own scope and redirect_url here
    scope = '' 
    redirect_url = ''

    flow = flow_from_clientsecrets('./client_secrets.json',
                                   scope,
                                   redirect_url)
    return flow

def get_auth_uri(flow):
    """Provide the API keys and receive a temporary code in return"""

    code = OAuth2WebServerFlow(client_id=flow.client_id,
                           client_secret=flow.client_secret,
                           scope=flow.scope,
                           redirect_uri=flow.redirect_uri)

    auth_uri = flow.step1_get_authorize_url()

    return auth_uri


class AuthUser(webapp2.RequestHandler):
    """Auth user via the Github API"""

    def get(self):

        # Create a flow object to begin Google flow workflow
        flow = create_flow_object()

        if not flow:
            self.error(404)         

        # Use the flow object to construct an authorization uri
        auth_uri = str(get_auth_uri(flow)) 
   
        if not auth_uri:
            self.error(404)

        self.redirect(auth_uri)
        return 


class RetrieveCode(webapp2.RequestHandler):
    """Switch the temporary code for an access token"""

    def get(self):

        # Get the code out of the url
        url = self.request.url 
        parsed_url = parse_qs(urlparse(url).query)
        code = parsed_url['code'][0]
       
        flow = create_flow_object()

        # Create a Credentials object which will hold the access token
        credentials = flow.step2_exchange(code)
        
        # Store the credentials object in the datastore
        storage = StorageByKeyName(CredentialsModel, 
                                   'auth_token', 'credentials')        

        storage.put(credentials)

        # EXAMPLE: to get the access token out of storage
        creds = storage.get()
        print(creds.access_token)
        return


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': ''  # use secret key
}

application = webapp2.WSGIApplication([
    ('/', AuthUser),
    ('/code', RetrieveCode),
], config=config, debug=True)
