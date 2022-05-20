import pyrebase
from requests.models import HTTPError
from flask import session

def firebase_initialize():
    firebase_config = {
      
    }

    firebase = pyrebase.initialize_app(firebase_config)
    auth = firebase.auth()
    return auth

def login(email, password):
    auth = firebase_initialize()
    try:
        auth.sign_in_with_email_and_password(email,password)
        session["email"] = email
        session["password"] = password
        session["username"] = email.split("@")[0]
        return True
    except HTTPError as e:
      return False

def signup(email, password):
    auth = firebase_initialize()
    try:
        auth.create_user_with_email_and_password(email,password)
        return True
    except HTTPError as e:
      return False

