from app import app
from flask import render_template


@app.route("/path", methods=["POST","GET"])
def home_view():
    
    return render_template('path/home.html', login=True)
