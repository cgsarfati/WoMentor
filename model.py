"""Models and database functions for WoMentor"""

from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime



db = SQLAlchemy()


# Model definitions

class Role(db.Model):

    __tablename__ = "roles"

    role_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    role=  db.Column(db.String(100), nullable=True)

class Location(db.Model):

    __tablename__ = "locations"

    loc_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    location=  db.Column(db.String(100), nullable=True)

class Level(db.Model):

    __tablename__ = "levels"

    level_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    level=  db.Column(db.String(100), nullable=True)

class Language(db.Model):

    __tablename__ = "languages"

    lag_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    languages=  db.Column(db.String(50), nullable=True)

class Day(db.Model):

    __tablename__ = "days"

    day_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    day=  db.Column(db.String(50), nullable=True)

class Activity(db.Model):

    __tablename__ = "activities"

    act_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    activity=  db.Column(db.String(100), nullable=True)


# Association tables


class u_location(db.Model):

    __tablename__ = "u_locations"

    u_location_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    loc_id = db.Column(db.Integer, db.ForeignKey('locations.loc_id'))


class u_level(db.Model):

    __tablename__ = "u_levels"

    u_level_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.level_id'))


class u_language(db.Model):

    __tablename__ = "u_languages"

    u_lang_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    lang_id = db.Column(db.Integer, db.ForeignKey('languages.lang_id'))

class u_day(db.Model):

    __tablename__ = "u_days"

    u_day_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    day_id = db.Column(db.Integer, db.ForeignKey('days.day_id'))


class u_activity(db.Model):

    __tablename__ = "u_activities"

    u_act_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    act_id = db.Column(db.Integer, db.ForeignKey('activities.act_id'))




class User(db.Model):
    """Users info Mentor/Mentee info"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    bio 
    name    
    email   
    nickname    
    job_title   
    match_id

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s name =%s email=%s>" % (self.user_id, self.
                                               self.email)


