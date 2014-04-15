"""
The model that the Credentials object uses to store and retrieve the access
token from the datastore.
"""

from google.appengine.ext import db
from oauth2client.appengine import CredentialsProperty


class CredentialsModel(db.Model):
    credentials = CredentialsProperty()
