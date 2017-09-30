"""Models and database functions for WoMentor"""

from flask_sqlalchemy import SQLAlchemy


=======
from datetime import date, datetime




db = SQLAlchemy()


# Model definitions

class Role(db.Model):

    __tablename__ = "roles"

    role_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    role=  db.Column(db.String(100), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Roles role_id=%s role=%s>" % (self.role_id, self.
                                               self.role)


=======
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

=======
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


=======

class Language(db.Model):

    __tablename__ = "languages"

    lag_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    language=  db.Column(db.String(50), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Languages lang_id=%s language=%s>" % (self.lang_id, self.
                                               self.language)

=======
    languages=  db.Column(db.String(50), nullable=True)


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


=======

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


=======


# Association tables


class u_location(db.Model):

    __tablename__ = "u_locations"

    u_location_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    loc_id = db.Column(db.Integer, db.ForeignKey('locations.loc_id'))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User location user_id=%s loc_id =%s>" % (self.user_id, self.
                                               self.loc_id)



=======

class u_level(db.Model):

    __tablename__ = "u_levels"

    u_level_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.level_id'))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User Level user_id=%s level_id =%s>" % (self.user_id, self.
                                               self.level_id)


=======


class u_language(db.Model):

    __tablename__ = "u_languages"

    u_lang_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    lang_id = db.Column(db.Integer, db.ForeignKey('languages.lang_id'))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User languages user_id=%s lang_id =%s>" % (self.user_id, self.
                                               self.lang_id)


=======

class u_day(db.Model):

    __tablename__ = "u_days"

    u_day_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    day_id = db.Column(db.Integer, db.ForeignKey('days.day_id'))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User's availability user_id=%s day_id =%s>" % (self.user_id, self.
                                               self.day_id)



=======

class u_activity(db.Model):

    __tablename__ = "u_activities"

    u_act_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    act_id = db.Column(db.Integer, db.ForeignKey('activities.act_id'))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User activities user_id=%s act_id =%s>" % (self.user_id, self.
                                               self.act_id)



class User(db.Model):
    """Users (Mentor/Mentee) info"""
=======


class User(db.Model):
    """Users info Mentor/Mentee info"""


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
=======
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


        return "<User user_id=%s role=%s job_title=%s> match_id=%s" % (self.user_id, self.
                                               self.role_id, self.job_title, self.job_title)
=======
        return "<User user_id=%s name =%s email=%s>" % (self.user_id, self.
                                               self.email)



