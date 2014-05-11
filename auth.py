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

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.appengine import StorageByKeyName

from basehandler import BaseHandler
from config import config
from model import CredentialsModel


GITHUB_API_URL = 'https://api.github.com'


def fetch_url(url, method=urlfetch.GET, data=''):
    """Send a HTTP request"""

    result = urlfetch.fetch(url=url, method=method, payload=data,
                            headers={'Access-Control-Allow-Origin': '*'})

    return result.content


def get_user_name():
    """Get the name of the current user"""

    url = '{}/user?access_token={}'.format(GITHUB_API_URL, get_access_token())

    result = json.loads(fetch_url(url))

    return result['login']


def _create_flow_object():
    """Check if client_secrets.json is populated"""

    flow = flow_from_clientsecrets('./client_secrets.json',
                                   scope='user,repo',
                                   redirect_uri='http://localhost:8080/code')

    return flow


def _get_auth_uri(flow):
    """Provide the API keys and receive a temporary code in return"""

    OAuth2WebServerFlow(client_id=flow.client_id,
                        client_secret=flow.client_secret,
                        scope=flow.scope,
                        redirect_uri=flow.redirect_uri)

    auth_uri = flow.step1_get_authorize_url()

    return auth_uri


def get_access_token():
    """Used to check app activation and append token to urls"""

    # Check if access token is in storage
    storage = StorageByKeyName(CredentialsModel, 'token', 'credentials')

    credentials = storage.get()

    if not credentials:
        return False

    return credentials.access_token


def _delete_access_token():
    """Delete access token from storage"""

    storage = StorageByKeyName(CredentialsModel, 'token', 'credentials')
    storage.delete()


def _retrieve_code(url):
    """Retrieve code from url"""

    parsed_url = parse_qs(urlparse(url).query)
    code = parsed_url['code'][0]
    return code


class DetectActivation(BaseHandler):
    """Detect if the app is set up"""

    def get(self):

        if not get_access_token() or not self.session.get('logged_in'):
            # App is not set up or user is not logged in
            self.redirect('/auth')
            return

        # Everything checks out, send user to auth
        self.redirect('/app')


class AuthUser(webapp2.RequestHandler):
    """Auth user via the Github API"""

    def get(self):

        # If User doesn't have Webfilings account, bail
        user = users.get_current_user()

        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        # Begin Google's flow workflow
        flow = _create_flow_object()

        if not flow:
            self.error(500)
            return

        # Use the flow object to construct an authorization uri
        auth_uri = str(_get_auth_uri(flow))

        if not auth_uri:
            self.error(500)
            return

        # After Github auth's the user, it returns them to
        # the authorization callback URL used in the apps' GH settings
        self.redirect(auth_uri)
        return


class RetrieveToken(BaseHandler):
    """Switch the temporary code for an access token"""

    def get(self):

        if get_access_token():
            # App is set up,send them to the front page
            self.session['logged_in'] = True
            self.redirect('/app')
            return

        # Get the code out of the url
        code = _retrieve_code(self.request.url)

        # Create a Credentials object which will hold the access token
        flow = _create_flow_object()
        credentials = flow.step2_exchange(code)

        # Store the access token, app is now activated
        storage = StorageByKeyName(CredentialsModel, 'token', 'credentials')
        storage.put(credentials)

        # User is logged in
        self.session['logged_in'] = True

        context = {
            "username": get_user_name(),
        }

        # Tell user that the app is activated
        self.render('index', context)


class Logout(BaseHandler):
    """Clear session variables and send to Github logout page"""

    def get(self):

        # Delete session vars
        self.session.clear()

        # Redirect to Github logout
        self.redirect('https://github.com/logout')


config = config()

app = webapp2.WSGIApplication([
    ('/', DetectActivation),
    ('/auth', AuthUser),
    ('/code', RetrieveToken),
    ('/logout', Logout),
], config=config, debug=True)
