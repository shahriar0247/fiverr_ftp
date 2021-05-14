import pyrebase
from requests.models import HTTPError
from flask import session

def firebase_initialize():
    firebase_config = {
        "apiKey": "AIzaSyCXALNlXRdJrcsRHro_4mdysZbi-mkCP0U",
        "authDomain": "indian-cloud-storage-fiverr.firebaseapp.com",
        "projectId": "indian-cloud-storage-fiverr",
        "storageBucket": "indian-cloud-storage-fiverr.appspot.com",
        "messagingSenderId": "728035506508",
        "appId": "1:728035506508:web:e5200e5276759bc45df7e9",
        "measurementId": "G-J575XZM3PT",
        "databaseURL": "",
    }

    firebase = pyrebase.initialize_app(firebase_config)
    auth = firebase.auth()
    return auth

def login(email, password):
    auth = firebase_initialize()
    try:
        auth.create_user_with_email_and_password(email,password)
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

