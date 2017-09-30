"""WoMentor web app"""

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

from model import (User, connect_to_db, db)


app = Flask(__name__)

# For Flask sessions and debug toolbar
app.secret_key = "ABC"

# Undefined variables in Jinja2 fail silently, raise an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Landing page of WoMentor"""

    return render_template("index.html")


@app.route('/register', method=['GET'])
def register():
    """Allows a user to register for WoMentor"""

    return render_template("register.html")


@app.route('/user{user.user_id}')
def profile(user_id):
    """Shows user profile page"""

    return render_template("user.html")


@app.route('/main', method=['GET'])
def mainpage():
    """Main interaction page where mentors/mentees find each other"""

    return render_template("main.html")


@app.route('/main', method=['POST'])
def results():
    """Shows match and scheduling between mentors/mentees"""

    return render_template("main.html")


###################################################
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
