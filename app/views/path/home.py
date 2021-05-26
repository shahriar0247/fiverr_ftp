
import io
from os import error

from flask.helpers import send_file
from app.functions.path import create_folder, delete_file, download_file2, get_all_folders, upload_files
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
            errors = json.loads(errors)
            return render_template('path/home.html', all_folders=all_folders, errors=errors)
    except KeyError: pass
    return redirect("/login")

@app.route("/create_folder", methods=["POST"])
def create_folder_view():
    create_folder(request.form.get("folder_name"), request.form.get("path"))
    return redirect("/?path=" + request.form.get("path"))

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

@app.route('/dd/<filename>', methods=["POST"])
def dd_view(filename):
    path = request.form.get("path")
    fun_type = request.form.get("type")
    element_name = request.form.get("element_name")
    if fun_type == "delete":
        error = delete_file(element_name, path)
        if error != None:
            session["error"] = json.dumps([error])
    elif fun_type == "download":
        binary, content_type, filename = download_file2(element_name, path)
        return send_file(
                     io.BytesIO(binary),
                     attachment_filename=filename,
                     mimetype=content_type
               )
    return redirect("/?path=" + path)

    