from flask.globals import request
from app import app
from flask import render_template, request


@app.route("/", methods=["POST","GET"])
def home_view():
    all_folders = get_all_folders(request.form.args("path"))
    return render_template('path/home.html', all_folders=all_folders)
