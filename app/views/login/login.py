from flask.globals import session
from werkzeug.utils import redirect
from app.functions.firebase_log import login, signup
from app import app
from flask import render_template, request


@app.route("/login", methods=["POST","GET"])
def login_view():
    if request.method == "POST":
        email  = request.form.get("email")
        password = request.form.get("password")
        session["username"] = email.split("@")[0]
        return redirect("/")
    return render_template('login/login.html', login=True)


@app.route("/register", methods=["POST","GET"])
def register_view():
    if request.method == "POST":
        email  = request.form.get("email")
        password = request.form.get("password")
        return redirect("/")
    return render_template('login/login.html', login=False)