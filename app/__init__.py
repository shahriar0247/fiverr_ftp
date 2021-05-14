from flask import Flask



app = Flask(__name__)

app.secret_key = "this iadfj alds jflakdsjfakdsl jfdslkfjdas;lkf ja;sldjkfalsd;kjf dalskjfa"


from app.views.login import login