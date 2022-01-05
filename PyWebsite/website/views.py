#views.py basically draws routes around how the users can taverse through the application. From login to welcome, welcome to home, home to logout etc.

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#first view/route
# this will work when the '/' is called by the user in the browser. So, technically the home page
@views.route('/')
def home():
    return render_template("home.html")
#register this view in init.py
