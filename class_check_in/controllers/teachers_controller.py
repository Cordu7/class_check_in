from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.teacher import Teacher
import repositories.teacher_repository as teacher_repository


teachers_blueprint = Blueprint("teachers", __name__)

@teachers_blueprint.route("/teachers")
def teachers():
    teachers = teacher_repository.select_all() 
    return render_template("teachers/index.html", teachers = teachers)

    

# NEW
# GET '/books/new'
@teachers_blueprint.route("/teachers/new")
def new_teacher():
    #teachers = teacher_repository.select_all()
    #return render_template("teachers/new.html", teachers = teachers)
    return render_template("teachers/new.html")

# CREATE
@teachers_blueprint.route("/teachers",  methods=['POST'])
def create_teacher():
    f_name    = request.form['f_name']
    l_name = request.form['l_name']    
    new_teacher = Teacher(f_name, l_name)
    teacher_repository.save(new_teacher)
    return redirect("/teachers")


# SHOW
# GET '/books/<id>'
# @teachers_blueprint.route("/teachers/<id>", methods=['GET'])
# def show_teacher(id):
#     teacher = teacher_repository.select(id)
#     return render_template('teachers/teachers/show.html', teacher = teacher)

# EDIT
# GET '/books/<id>/edit'
@teachers_blueprint.route("/teachers/<id>/edit")
def edit_teacher(id):
    teacher = teacher_repository.select(id)
    return render_template('teachers/edit.html', teacher = teacher)

# UPDATE
# PUT '/books/<id>'
@teachers_blueprint.route("/teachers/<id>", methods=['POST'])
def update_teacher(id):
    #teacher= teacher_repository.select(id)
    f_name  = request.form['f_name']
    l_name = request.form['l_name']
    teacher = Teacher(f_name, l_name, id)
    teacher_repository.update(teacher)
    return redirect('/teachers')

# DELETE
# DELETE '/books/<id>'
@teachers_blueprint.route("/teachers/<id>/delete", methods=['POST'])
def delete_teacher(id):
    teacher_repository.delete(id)
    return redirect('/teachers')
