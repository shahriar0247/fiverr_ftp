
from app.functions.path import create_folder, get_all_folders


from app import app
from flask import render_template, request, session, redirect


@app.route("/")
def home_view():
    try:
        if session["username"] != "empty":
            all_folders = get_all_folders(request.args.get("path"))
            
            return render_template('path/home.html', all_folders=all_folders)
    except KeyError: pass
    return redirect("/login")

@app.route("/create_folder", methods=["POST"])
def create_folder_view():
    create_folder(request.form.get("folder_name"), request.form.get("path"))