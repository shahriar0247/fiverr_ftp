from flask import Flask



app = Flask(__name__)

app.secret_key = "this iasdasdkjfa"


from app.views.login import login

from app.views.path import home