"""Models and database functions for WoMentor"""

from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()


# Model definitions

class Role(db.Model):

    __tablename__ = "roles"

    role_id= db.Column(db.Integer,
                        autoincrement=False,
                        primary_key=True)
    role=  db.Column(db.String(25), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Roles role_id=%s role=%s>" % (self.role_id, self.
                                               self.role)

    #relationship Role / User
    user = db.relationship("User", backref="roles")


class Location(db.Model):

    __tablename__ = "locations"

    loc_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    location=  db.Column(db.String(100), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Locations loc_id=%s location=%s>" % (self.loc_id, self.
                                               self.location)

class Level(db.Model):

    __tablename__ = "levels"

    level_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    level=  db.Column(db.String(100), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Levels level_id=%s level=%s>" % (self.level_id, self.
                                               self.level)


class Language(db.Model):

    __tablename__ = "languages"

    lang_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    language=  db.Column(db.String(50), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Languages lang_id=%s language=%s>" % (self.lang_id, self.
                                               self.language)


class Day(db.Model):

    __tablename__ = "days"

    day_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    day=  db.Column(db.String(50), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Days day_id=%s day=%s>" % (self.day_id, self.
                                               self.day)


class Activity(db.Model):

    __tablename__ = "activities"

    act_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    activity=  db.Column(db.String(100), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Activities act_id=%s activity=%s>" % (self.act_id, self.
                                               self.activity)



# Association tables


class u_location(db.Model):

    __tablename__ = "u_locations"

    u_location_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    loc_id = db.Column(db.Integer, db.ForeignKey('locations.loc_id'))

    #many to many relationship between locations and users
    location = db.relationship("Location", backref="u_locations")
    user = db.relationship("User", backref="u_locations")


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User location user_id=%s loc_id =%s>" % (self.user_id, self.
                                               self.loc_id)



class u_level(db.Model):

    __tablename__ = "u_levels"

    u_level_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.level_id'))

    #many to many relationship between levels and users
    level = db.relationship("Level", backref="u_levels")
    user = db.relationship("User", backref="u_levels")


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User Level user_id=%s level_id =%s>" % (self.user_id, self.
                                               self.level_id)



class u_language(db.Model):

    __tablename__ = "u_languages"

    u_lang_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    lang_id = db.Column(db.Integer, db.ForeignKey('languages.lang_id'))

    #many to many relationship between languages and users
    language = db.relationship("Language", backref="u_languages")
    user = db.relationship("User", backref="u_languages")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User languages user_id=%s lang_id =%s>" % (self.user_id, self.
                                               self.lang_id)


class u_day(db.Model):

    __tablename__ = "u_days"

    u_day_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    day_id = db.Column(db.Integer, db.ForeignKey('days.day_id'))

    #many to many relationship between days and users
    day = db.relationship("Day", backref="u_day")
    user = db.relationship("User", backref="u_day")


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User's availability user_id=%s day_id =%s>" % (self.user_id, self.
                                               self.day_id)



class u_activity(db.Model):

    __tablename__ = "u_activities"

    u_act_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    act_id = db.Column(db.Integer, db.ForeignKey('activities.act_id'))

    #many to many relationship between activities and users
    activity = db.relationship("Activity", backref="u_activities")
    user = db.relationship("User", backref="u_activities")



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User activities user_id=%s act_id =%s>" % (self.user_id, self.
                                               self.act_id)



class User(db.Model):
    """Users (Mentor/Mentee) info"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    role_id = db.Column(db.Integer, 
                        db.ForeignKey('roles.role_id'))
    bio = db.Column(db.String(100), nullable=True) 
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    nickname = db.Column(db.String(25), nullable=True)    
    job_title = db.Column(db.String(100), nullable=True)  
    match_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s role=%s job_title=%s> match_id=%s" % (self.user_id, self.
                                               self.role_id, self.job_title, self.job_title)

# Helper functions

def init_app():

    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB"

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///womentor'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

def upload_Data():

    Location.query.delete()

    sanFrancisco = Location(location="San Francisco")
    eastBay = Location(location="East Bay")
    southBay = Location(location="South Bay")
    northBay = Location(location="North Bay")
    peninsula = Location(location="Peninsula")

    Level.query.delete()

    beginner = Level(level="Beginner")
    intermediate = Level(level="Intermediate")
    advance = Level(level= "Advance")

    Language.query.delete()

    english = Language(language="English")
    spanish = Language(language="Spanish")
    mandarin = Language(language="Mandarin")

    Day.query.delete()

    monday = Day(day="Monday")
    tuesday = Day(day="Tuesday")
    wednesday = Day(day="Wednesday")
    thursday = Day(day="Thursday")
    friday = Day(day="Friday")
    saturday = Day(day="Saturday")
    sunday = Day(day="Sunday")

    Activity.query.delete()

    whiteboarding = Activity(activity="Whiteboarding")
    interview_practice = Activity(activity="Interview Practice")
    code_review = Activity(activity="Code review")
    general_info = Activity(activity="General Info")

    Role.query.delete()

    mentor = Role(role_id=1, role="Mentor")
    mentee = Role(role_id=2, role="Mentee")

    db.session.add_all([sanFrancisco, eastBay, southBay, northBay, peninsula,
                        beginner, intermediate,advance,
                        english, spanish, mandarin,
                        monday, tuesday, wednesday, thursday, friday, saturday, sunday,
                        whiteboarding, interview_practice, code_review, general_info, mentor, mentee])
    db.session.commit()





if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB :)"
<<<<<<< HEAD
    print app.config['SQLALCHEMY_TRACK_MODIFICATIONS']
=======
    
>>>>>>> master
    # db.create_all()
    # upload_Data()
