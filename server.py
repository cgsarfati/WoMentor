"""WoMentor web app"""

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

from model import (User, Language, u_language, Day, u_day, Location,
                   u_location, Level, u_level, Activity, u_activity,
                   connect_to_db, db)


app = Flask(__name__)

# For Flask sessions and debug toolbar
app.secret_key = "ABC"

# Undefined variables in Jinja2 fail silently, raise an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Landing page of WoMentor"""

    return render_template("home.html")


@app.route('/register', methods=['GET'])
def register():
    """Allows a user to register for WoMentor"""

    return render_template("register.html")


@app.route('/register', methods=['POST'])
def registered():
    """Parses registration form data"""

    # Check language capabilities of user
    # TODO: figure out how to get the user
    english = request.form.get("english")
    spanish = request.form.get("spanish")
    mandarin = request.form.get("mandarin")

    langs = ([english, spanish, mandarin])
    langs.remove(None)


    # Add user languages to db
    for lang in langs:
        language = db.session.query(Language).filter(Language.language == lang).one()
        new_lang = u_language(user_id=user_id, lang_id=lang)
        db.session.add(new_lang)
    db.session.commit()

    # Check availability of user
    mon = request.form.get("monday")
    tues = request.form.get("tuesday")
    wed = request.form.get("wednesday")
    thurs = request.form.get("thursday")
    fri = request.form.get("friday")
    sat = request.form.get("saturday")
    sun = request.form.get("sunday")

    avail = {mon, tues, wed, thurs, fri, sat, sun}
    avail.remove(None)

    # Add user availability to db
    for time in avail:
        free = db.session.query(Day).filter(day_id == time)
        new_avail = u_days(user_id=user_id, day_id=free)
        db.session.add(new_avail)
    db.session.commit()

    # Add user location to db
    loc = request.form.get("location")
    location = db.session.query(Location).filter(location == loc)
    new_loc = u_location(user_id=user_id, loc_id=location)
    db.session.add(new_loc)
    db.session.commit()

    # Add user level to db
    level = request.form.get("level")
    code_level = db.session.query(Level).filter(level == level)
    new_level = u_level(user_id=user_id, level_id=level)
    db.session.add(new_level)
    db.session.commit()

    # Add users requested activity to db
    activity = request.form.get('activity')
    act = db.session.query(Activity).filter(activity == activity)
    new_act = u_activity(user_id=user_id, act_id=act)
    db.session.add(new_act)
    db.session.commit()

    return redirect('/register')


@app.route('/user/{user_id}')
def profile(user_id):
    """Shows user profile page"""

    user = User.query.get(user_id)

    return render_template("profile.html", user=user)


@app.route('/main')
def mainpage():
    """Main interaction page where mentors/mentees find each other"""

    return render_template("main.html")


@app.route('/main', methods=['POST'])
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
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
