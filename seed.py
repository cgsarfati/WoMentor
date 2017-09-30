"""Seeds system data into db"""

import sqlalchemy
from server import app
from model import connect_to_db, db
# from model import all the tables
import random
#*****************************************************************************#

# LEVELS = ["beginner", "intermediate", "advanced"]
# LOCATIONS = ["San Francisco", "East Bay", "South Bay", "North Bay", "Peninsula"]
# LANGUAGES = ["English", "Spanish", "Mandarin"]
# DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# ACTIVITIES = ["whiteboarding", "interview practice", "code review", "general info"]

def load_users(file, num):
    """Load fake mentees and mentors for testing from file"""

    # if this file is run more than once, deletes prior data
    User.query.delete()

    for row in open(file):
        row = row.rstrip()
        user_id, bio, name, email, nickname, job_title = row.split(",")
        
        # locations = random.choice(LOCATIONS)
        # languages = random.choice(LANGUAGES)
        # days = random.choice(DAYS)
        # activities = random.choice(ACTIVITIES)

        user = User(user_id=user_id, role_id=num, bio=bio, name=name,
                    email=email, nickname=nickname, job_title=job_title)

        db.session.add(user)
        db.session.commit()

def load_levels():
    """Load fake levels for all users"""
    
    users = db.session.query(User.user_id).all()
    level_id = db.session.query(Levels.level_id).all()

    for user in users:
        # get a random level id
        user_level_id = random.choice(level_id)
        level = U_Level(user_id=user, level_id=user_level_id)

        db.session.add(level)
        db.session.commit()


def load_locations():
    """Load fake locations for all users"""
    
    users = db.session.query(User.user_id).all()
    location_id = db.session.query(Locations.loc_id).all()

    for user in users:
        # get a random location
        user_location_id = random.choice(location_id)
        location = U_Location(user_id=user, loc_id=user_location_id)

        db.session.add(location)
        db.session.commit()

def load_languages():
    """Load fake languages for all users"""
    
    users = db.session.query(User.user_id).all()
    language_id = db.session.query(Languages.lang_id).all()

    for user in users:
        # get a random language
        user_language_id = random.choice(language_id)
        language = U_Languages(user_id=user, lang_id=user_language_id)

        db.session.add(language)
        db.session.commit()

def load_days():
    """Load fake availability for all users

    Current implementation loads ONE available day per user.

    """
    
    users = db.session.query(User.user_id).all()
    day_id = db.session.query(Days.day_id).all()

    for user in users:
        # get a random day
        user_day_id = random.choice(day_id)
        day = U_Days(user_id=user, day_id=user_day_id)

def load_activities():
    """Load fake activities for all users"""
    pass

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

    # last fuunction
    set_val_user_id()
    print "Seeding complete!"