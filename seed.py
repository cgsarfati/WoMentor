"""Seeds system data into db"""

import sqlalchemy
from server import app
# from model import connect_to_db, db
from model import connect_to_db, db
from model import User, Location, Level, Language, Day, Activity, u_location, u_level, u_language, u_day, u_activity
import random
#*****************************************************************************#

def load_users(file, num):
    """Load fake mentees and mentors for testing from file"""

    # if this file is run more than once, deletes prior data
    User.query.delete()

    for row in open(file):
        row = row.rstrip()
        user_id, bio, name, email, nickname, job_title = row.split(",")
        
        user = User(user_id=user_id, name=name, email=email, role_id=num, 
                    bio=bio, nickname=nickname, job_title=job_title)

        db.session.add(user)
        db.session.commit()

def load_levels():
    """Load fake levels for all users"""

    u_level.query.delete()
    
    users = db.session.query(User.user_id).all()
    level_id = db.session.query(Level.level_id).all()

    for user in users:
        # get a random level id
        user_level_id = random.choice(level_id)
        level = u_level(user_id=user, level_id=user_level_id)

        db.session.add(level)
        db.session.commit()


def load_locations():
    """Load fake locations for all users"""

    u_location.query.delete()
    
    users = db.session.query(User.user_id).all()
    location_id = db.session.query(Location.loc_id).all()

    for user in users:
        # get a random location
        user_location_id = random.choice(location_id)
        location = u_location(user_id=user, loc_id=user_location_id)

        db.session.add(location)
        db.session.commit()

def load_languages():
    """Load fake languages for all users"""

    u_language.query.delete()
    
    users = db.session.query(User.user_id).all()
    language_id = db.session.query(Language.lang_id).all()

    for user in users:
        # get a random language
        user_language_id = random.choice(language_id)
        language = u_language(user_id=user, lang_id=user_language_id)

        db.session.add(language)
        db.session.commit()

def load_days():
    """Load fake availability for all users

    Current implementation loads ONE available day per user.

    """

    u_day.query.delete()
    
    users = db.session.query(User.user_id).all()
    day_id = db.session.query(Day.day_id).all()

    for user in users:
        # get a random day
        user_day_id = random.choice(day_id)
        day = u_day(user_id=user, day_id=user_day_id)

def load_activities():
    """Load fake activities for all users

    Current implementation loads ONE activity per user.
    """

    u_activity.query.delete()
    
    users = db.session.query(User.user_id).all()
    activity_id = db.session.query(Activity.act_id).all()

    for user in users:
        # get a random activity
        user_act_id = random.choice(activity_id)
        activity = u_activity(user_id=user, act_id=user_act_id)

def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()

#*****************************************************************************#

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.drop_all()
    db.create_all()

    mentors = "seed_data/mock_mentees.csv"
    mentees = "seed_data/mock_mentors.csv"

    load_users(mentors, 1)
    print "Loaded mentors to user table"
    load_users(mentees, 2)
    print "Loaded mentees to user table"
    load_levels()
    print "Loaded levels for all users"
    load_locations()
    print "Loaded locations for all users"
    load_languages()
    print "Loaded languages for all users"
    load_days()
    print "Loaded availability for all users"
    load_activities()
    print "Loaded activities for all users"

    set_val_user_id()
    print "Seeding complete!"