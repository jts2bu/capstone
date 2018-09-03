import sqlalchemy
import datetime

class Person(db.model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(20), unique = False, nullable = False)
    lastname = db.Column(db.String(20), unique = False, nullable = False)
    birthday = db.Column(db.String(10), unique = False, nullable = False)

    universityID = db.Column(db.String(9), unique = False, nullable = False)
    computingID = db.Column(db.String(5), unique = False, nullable = False)


class Building(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)


class Entry(db.model):
    id = db.Column(db.Integer, primary_key = True)
    time = db.Column(db.DateTime, unique = False, nullable = False)

    firstname = db.Column(db.String(20), unique = False, nullable = False)
    lastname = db.Column(db.String(20), unique = False, nullable = False)
    birthday = db.Column(db.String(10), unique = False, nullable = False)

    universityID = db.Column(db.String(9), unique = False, nullable = False)
    computingID = db.Column(db.String(5), unique = False, nullable = False)
