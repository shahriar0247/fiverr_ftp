from werkzeug.utils import redirect
from app.functions.path import get_all_folders
from flask.globals import request

from app import app
from flask import render_template, request, session


@app.route("/", methods=["POST","GET"])
def home_view():
    try:
        if session["username"] != "empty":
            all_folders = get_all_folders(request.form.args("path"))
            return render_template('path/home.html', all_folders=all_folders)
    except KeyError: pass
    return redirect("/login")