from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.teacher import Teacher
import repositories.teacher_repository as teacher_repository


teachers_blueprint = Blueprint("teachers", __name__)

@teachers_blueprint.route("/teachers")
def teachers():
    teachers = teacher_repository.select_all() 
    return render_template("teachers/index.html", teachers = teachers)

@teachers_blueprint.route("/teachers/new")
def new_teacher():
    return render_template("teachers/new.html")

# CREATE
@teachers_blueprint.route("/teachers",  methods=['POST'])
def create_teacher():
    title   = request.form['title']
    name = request.form['name']    
    new_teacher = Teacher(title, name)
    teacher_repository.save(new_teacher)
    return redirect("/teachers")

@teachers_blueprint.route("/teachers/<id>/edit")
def edit_teacher(id):
    teacher = teacher_repository.select(id)
    return render_template('teachers/edit.html', teacher = teacher)

@teachers_blueprint.route("/teachers/<id>", methods=['POST'])
def update_teacher(id):
    title  = request.form['title']
    name = request.form['name']
    teacher = Teacher(title, name, id)
    teacher_repository.update(teacher)
    return redirect('/teachers')

@teachers_blueprint.route("/teachers/<id>/delete", methods=['POST'])
def delete_teacher(id):
    teacher_repository.delete(id)
    return redirect('/teachers')
