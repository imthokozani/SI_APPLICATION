import os
from flask import Blueprint, current_app, make_response, redirect, render_template, request
from . import db
from WEBSITE.models import Student, Student_Registration
import qrcode

views = Blueprint('views', __name__)

@views.route("/regs")
def view_regs():
    users = Student_Registration.query.all()
    return "<br>".join([f"{u.id} - {u.date} {u.student_id}" for u in users])

@views.route("/users")
def view_users():
    users = Student.query.all()
    return "<br>".join([f"{u.id} - {u.name} {u.surname}" for u in users])

@views.route('/qrcode')
def gen_qrcode():
    data = "https://web-production-9375.up.railway.app/"
    qr = qrcode.make(data)
    
    static_folder = current_app.static_folder
    file_path = os.path.join(static_folder, "qrcode.jpeg")
    qr.save(file_path)
    return render_template('qrcode.html')

@views.route('/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        u_student_number = request.form.get('student_number')
        user = Student.query.filter_by(student_number = u_student_number).first()
        if user != None:
            new_learner_reg = Student_Registration(student_id = user.id)
            db.session.add(new_learner_reg)
            db.session.commit()    
        else:
            print("error: user does not exists")
    return render_template('register.html')

@views.route('/add_learners', methods=['GET','POST'])
def add_learner():
    if request.method == 'POST':
        u_student_number = request.form.get('student_number')
        user = Student.query.filter_by(student_number = u_student_number).first()
        if user == None:
            u_name = request.form.get('name')
            u_surname = request.form.get('surname')
            new_student = Student(student_number = u_student_number, name = u_name, surname = u_surname)
            db.session.add(new_student)
            db.session.commit()
            print("learner successfully added")
        else:
            print("learner with this student number already exists")
    return render_template('add_learner.html')
