
from app.functions.path import create_folder, get_all_folders, upload_files
import json
from app import app
from flask import render_template, request, session, redirect


@app.route("/")
def home_view():
    try:
        if session["username"] != "empty":
            all_folders = get_all_folders(request.args.get("path"))
            try:
                if session["error"] != "empty":
                    errors = session["error"]
                    session["error"] = "empty"
                else:
                    return render_template('path/home.html', all_folders=all_folders)
            except KeyError:
                return render_template('path/home.html', all_folders=all_folders)
            return render_template('path/home.html', all_folders=all_folders, errors=errors)
    except KeyError: pass
    return redirect("/login")

@app.route("/create_folder", methods=["POST"])
def create_folder_view():
    create_folder(request.form.get("folder_name"), request.form.get("path"))

@app.route("/upload_file", methods=["POST"])
def upload_file_view():
    uploaded_file = request.files.getlist("uploaded_file")

    filepath = request.form.get("filepath")

    errors = []
    for one_file in uploaded_file:

        error = (upload_files(one_file, filepath))
        if error != True:
            errors.append(error)
        
        session["error"] = json.dumps(errors)


    return redirect("/?path=" + filepath)