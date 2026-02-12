from sqlalchemy import func
from . import db
from datetime import date

class Learner(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    registrations = db.relationship('Learner_Reg')
    registrationss = db.relationship('Registration')
    registrationsss = db.relationship('Reg')

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('learner.id'))

class Reg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, default = date.today)
    user_id = db.Column(db.Integer, db.ForeignKey('learner.id'))

class Learner_Reg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('learner.id'))

""""new models that are going to be used"""

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    student_number = db.Column(db.String(9))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    registrations = db.relationship('Student_Registration')

class Student_Registration(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, default = date.today)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))