from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.student import Student
import repositories.pupil_repository as student_repository
import repositories.emotion_repository as emotion_repository
import repositories.subemotion_repository as subemotion_repository

import datetime
import pdb


students_blueprint = Blueprint("students", __name__)

@students_blueprint.route("/students")
def students():
    students = student_repository.select_all()
    emotion_low = emotion_repository.select(1)
    emotion_ready = emotion_repository.select(2)
    emotion_unsettled = emotion_repository.select(3)
    emotion_out= emotion_repository.select(4)
    return render_template("students/index.html", students = students, emotion_low=emotion_low, emotion_ready=emotion_ready, emotion_unsettled=emotion_unsettled, emotion_out=emotion_out)

@students_blueprint.route("/students/low")
def low():
    students = student_repository.select_all()
    emotion_low = emotion_repository.select(1)
    subemotions = subemotion_repository.select_by_emotion(emotion_low)  
    return render_template("students/low.html", students = students, subemotions=subemotions)

@students_blueprint.route("/students/ready")
def ready():
    students = student_repository.select_all()
    subemotions = subemotion_repository.select_all()
    return render_template("students/ready.html", students = students, subemotions=subemotions)


@students_blueprint.route("/students/unsettled")
def unsettled():
    students = student_repository.select_all()
    subemotions = subemotion_repository.select_all()   
    return render_template("students/unsettled.html", students = students, subemotions=subemotions)
  

@students_blueprint.route("/students/out-of-control")
def out_of_control():
    students = student_repository.select_all()
    subemotions = subemotion_repository.select_all()   
    return render_template("students/out-of-control.html", students = students, subemotions= subemotions)




# @pupils_blueprint.route("/pupils/new")
# def new_pupil():
#     teachers = teacher_repository.select_all() 
#     return render_template("teachers/pupils/new.html", teachers=teachers)

# # f_name, l_name, d_o_b, gender, teacher,
# # CREATE
# @pupils_blueprint.route("/pupils",  methods=['POST'])
# def create_pupil():
#     f_name  = request.form['f_name']
#     l_name = request.form['l_name']    
#     d_o_b = request.form['d_o_b'] 
#     split_date = d_o_b.split('-')  
#     d_o_b = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2])) 
#     gender= request.form['gender']    
#     teacher_id= request.form['teacher_id']
#     teacher = teacher_repository.select(teacher_id)   
#     new_pupil = Student(f_name, l_name, d_o_b, gender, teacher)
#     pupil_repository.save(new_pupil)
    
#     return redirect("/pupils")

#     # date_borrowed=request.form['date']
#     # split_date = date_borrowed.split('-')
#     # date_borrowed = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))


# # SHOW
# # GET '/books/<id>'
# @pupils_blueprint.route("/pupils/<id>")
# def show_pupil(id):
#     pupil = pupil_repository.select(id)
#     teacher=teacher_repository.select(pupil.teacher)
#     return render_template('teachers/pupils/show.html', pupil = pupil, teacher =teacher)



# # EDIT
# # GET '/books/<id>/edit'
# @pupils_blueprint.route("/pupils/<id>/edit")
# def edit_pupil(id):
#     pupil = pupil_repository.select(id)
#     teachers = teacher_repository.select_all()
#     return render_template('teachers/pupils/edit.html', pupil = pupil, teachers= teachers)

# # UPDATE
# # PUT '/books/<id>'
# @pupils_blueprint.route("/pupils/<id>", methods=['POST'])
# def update_pupil(id):
#     f_name  = request.form['f_name']
#     l_name = request.form['l_name']    
#     d_o_b = request.form['d_o_b'] 
#     split_date = d_o_b.split('-')  
#     d_o_b = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2])) 
#     gender= request.form['gender']    
#     teacher_id= request.form['teacher_id']
#     teacher = teacher_repository.select(teacher_id)   
#     new_pupil = Student(f_name, l_name, d_o_b, gender, teacher, id)
#     print(new_pupil.d_o_b)
#     pupil_repository.update(new_pupil)
#     return redirect('/pupils')


# # DELETE '/books/<id>'
# @pupils_blueprint.route("/pupils/<id>/delete", methods=['POST'])
# def delete_pupil(id):
#     pupil_repository.delete(id)
#     return redirect('/pupils')