"""Seeds system data into db"""

import sqlalchemy
from server import app
from model import connect_to_db, db
# from model import all the tables
import random
#*****************************************************************************#

LEVELS = ["beginner", "intermediate", "advanced"]
LOCATIONS = ["San Francisco", "East Bay", "South Bay", "North Bay", "Peninsula"]
LANGUAGES = ["English", "Spanish", "Mandarin"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ACTIVITIES = ["whiteboarding", "interview practice", "code review", "general info"]

def load_users(file):
    """Load fake mentees and mentors for testing from file"""

    # if this file is run more than once, deletes prior data
    User.query.delete()

    for row in open(file):
        row = row.rstrip()
        user_id, bio, name, email, nickname, job_title = row.split(",")

        level = random.choice(LEVELS)
        locations = random.choice(LOCATIONS)
        languages = random.choice(LANGUAGES)
        days = random.choice(DAYS)
        activities = random.choice(ACTIVITIES)


        user = User(user_id=user_id, bio=bio, name=name, email=email,
                    nickname=nickname, job_title=job_title)

        db.session.add(user)
        db.session.commit()
    # random.choice

    # load random availability

    # make 2, load mentors and load mentees so we have an even number of both

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

    load_users(mentors)
    print "Loaded mentors to user table"
    load_users(mentees)
    print "Loaded mentees to user table"

