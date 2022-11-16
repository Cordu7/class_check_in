from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.student import Student
import repositories.pupil_repository as pupil_repository
import repositories.teacher_repository as teacher_repository
import datetime
import pdb


pupils_blueprint = Blueprint("pupils", __name__)

@pupils_blueprint.route("/pupils")
def pupils():
    pupils = pupil_repository.select_all()
    teachers=teacher_repository.select_all()       
    return render_template("teachers/pupils/index.html", pupils = pupils, teachers=teachers)

# for pupil in pupils:
#         teacher=teacher_repository.select(pupil.teacher)
#  teachers=teacher_repository.select_all()


@pupils_blueprint.route("/pupils/new")
def new_pupil():
    teachers = teacher_repository.select_all() 
    return render_template("teachers/pupils/new.html", teachers=teachers)

# f_name, l_name, d_o_b, gender, teacher,
# CREATE
@pupils_blueprint.route("/pupils",  methods=['POST'])
def create_pupil():
    f_name  = request.form['f_name']
    l_name = request.form['l_name']    
    d_o_b = request.form['d_o_b'] 
    split_date = d_o_b.split('-')  
    d_o_b = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2])) 
    gender= request.form['gender']    
    teacher_id= request.form['teacher_id']
    teacher = teacher_repository.select(teacher_id)   
    new_pupil = Student(f_name, l_name, d_o_b, gender, teacher)
    pupil_repository.save(new_pupil)
    
    return redirect("/pupils")

    # date_borrowed=request.form['date']
    # split_date = date_borrowed.split('-')
    # date_borrowed = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))


# SHOW
# GET '/books/<id>'
@pupils_blueprint.route("/pupils/<id>")
def show_pupil(id):
    pupil = pupil_repository.select(id)
    teacher=teacher_repository.select(pupil.teacher)
    return render_template('teachers/pupils/show.html', pupil = pupil, teacher =teacher)



# EDIT
# GET '/books/<id>/edit'
@pupils_blueprint.route("/pupils/<id>/edit")
def edit_pupil(id):
    pupil = pupil_repository.select(id)
    teachers = teacher_repository.select_all()
    return render_template('teachers/pupils/edit.html', pupil = pupil, teachers= teachers)

# UPDATE
# PUT '/books/<id>'
@pupils_blueprint.route("/pupils/<id>", methods=['POST'])
def update_pupil(id):
    f_name  = request.form['f_name']
    l_name = request.form['l_name']    
    d_o_b = request.form['d_o_b'] 
    split_date = d_o_b.split('-')  
    d_o_b = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2])) 
    gender= request.form['gender']    
    teacher_id= request.form['teacher_id']
    teacher = teacher_repository.select(teacher_id)   
    new_pupil = Student(f_name, l_name, d_o_b, gender, teacher, id)
    print(new_pupil.d_o_b)
    pupil_repository.update(new_pupil)
    return redirect('/pupils')


# DELETE '/books/<id>'
@pupils_blueprint.route("/pupils/<id>/delete", methods=['POST'])
def delete_pupil(id):
    pupil_repository.delete(id)
    return redirect('/pupils')