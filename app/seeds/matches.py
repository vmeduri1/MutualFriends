from werkzeug.security import generate_password_hash
from app.models import db, User, Match

def seed_matches():
    # demo = User.query.filter_by(username="Demo")
    # markZ = User.query.filter_by(username="marky")
    # hieu = User.query.filter_by(username="hieu")
    # steveJ = User.query.filter_by(username="Jobs")

    demo_mark = Match(match_a=1, match_b=2)
    db.session.add(demo_mark)

    mark_demo = Match(match_a=2, match_b=1)
    db.session.add(mark_demo)

    demo_50 = Match(match_a = 50, match_b=1)
    db.session.add(demo_50)
    demo_49 = Match(match_a = 49, match_b=1)
    db.session.add(demo_49)
    demo_48 = Match(match_a = 48, match_b=1)
    db.session.add(demo_48)
    demo_47 = Match(match_a = 47, match_b=1)
    db.session.add(demo_47)
    demo_46 = Match(match_a = 46, match_b=1)
    db.session.add(demo_46)
    demo_45 = Match(match_a = 45, match_b=1)
    db.session.add(demo_45)
    demo_44 = Match(match_a = 44, match_b=1)
    db.session.add(demo_44)
    demo_43 = Match(match_a = 43, match_b=1)
    db.session.add(demo_43)
    demo_42 = Match(match_a = 42, match_b=1)
    db.session.add(demo_42)
    demo_41 = Match(match_a = 41, match_b=1)
    db.session.add(demo_41)
    demo_40 = Match(match_a = 40, match_b=1)
    db.session.add(demo_40)
    demo_39 = Match(match_a = 39, match_b=1)
    db.session.add(demo_39)
    demo_38 = Match(match_a = 38, match_b=1)
    db.session.add(demo_38)
    demo_37 = Match(match_a = 37, match_b=1)
    db.session.add(demo_37)
    demo_36 = Match(match_a = 36, match_b=1)
    db.session.add(demo_36)
    demo_35 = Match(match_a = 35, match_b=1)
    db.session.add(demo_35)

    demo_hieu = Match(match_a=1, match_b=3)
    db.session.add(demo_hieu)

    demo_jobs = Match(match_a=1, match_b=4)
    db.session.add(demo_jobs)

    demo_whitney = Match(match_a=1, match_b=5)
    # whitney_demo = Match(match_a=5, match_b=1)
    # db.session.add(whitney_demo)
    db.session.add(demo_whitney)

    elon_b = Match(match_a=12, match_b=13)
    db.session.add(elon_b)

    db.session.commit()

def undo_matches():
    db.session.execute('TRUNCATE matches RESTART IDENTITY CASCADE;')
    db.session.commit()
