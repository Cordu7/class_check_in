from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.student import Student
import repositories.pupil_repository as pupil_repository
import repositories.teacher_repository as teacher_repository
import repositories.feeling_repository as feeling_repository
import pdb


pupils_blueprint = Blueprint("pupils", __name__)

@pupils_blueprint.route("/pupils")
def pupils():
    pupils = pupil_repository.select_all()
    teachers=teacher_repository.select_all()       
    return render_template("teachers/pupils/index.html", pupils = pupils, teachers=teachers)

@pupils_blueprint.route("/pupils/new")
def new_pupil():
    teachers = teacher_repository.select_all() 
    return render_template("teachers/pupils/new.html", teachers=teachers)

# CREATE
@pupils_blueprint.route("/pupils",  methods=['POST'])
def create_pupil():
    name  = request.form['name']      
    teacher_id= request.form['teacher_id']
    teacher = teacher_repository.select(teacher_id)   
    new_pupil = Student(name, teacher)
    pupil_repository.save(new_pupil)
    return redirect("/pupils")

# SHOW
@pupils_blueprint.route("/pupils/<id>")
def show_pupil(id):
    pupil = pupil_repository.select(id)
    teacher=teacher_repository.select(pupil.teacher)
    return render_template('teachers/pupils/show.html', pupil = pupil, teacher =teacher)

# SHOW one students feelings
@pupils_blueprint.route("/pupils/<id>/feelings")
def one_student_feeling(id):
    student = pupil_repository.select(id)
    feelings = feeling_repository.select_by_student(student)
    return render_template("teachers/feelings/index.html", student = student, feelings=feelings)

# EDIT
@pupils_blueprint.route("/pupils/<id>/edit")
def edit_pupil(id):
    pupil = pupil_repository.select(id)
    teachers = teacher_repository.select_all()
    return render_template('teachers/pupils/edit.html', pupil = pupil, teachers= teachers)

# UPDATE
# PUT 
@pupils_blueprint.route("/pupils/<id>", methods=['POST'])
def update_pupil(id):
    name  = request.form['name']  
    teacher_id= request.form['teacher_id']
    teacher = teacher_repository.select(teacher_id)   
    new_pupil = Student(name, teacher, id)
    pupil_repository.update(new_pupil)
    return redirect('/pupils')

# DELETE 
@pupils_blueprint.route("/pupils/<id>/delete", methods=['POST'])
def delete_pupil(id):
    pupil_repository.delete(id)
    return redirect('/pupils')