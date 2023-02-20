from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.student import Student
import repositories.pupil_repository as student_repository
import repositories.emotion_repository as emotion_repository
import repositories.subemotion_repository as subemotion_repository
import repositories.feeling_repository as feeling_repository
from models.feeling import Feeling

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
    emotion_ready = emotion_repository.select(2)
    subemotions = subemotion_repository.select_by_emotion(emotion_ready) 
    return render_template("students/ready.html", students = students, subemotions=subemotions)


@students_blueprint.route("/students/unsettled")
def unsettled():
    students = student_repository.select_all()
    emotion_unsettled = emotion_repository.select(3)
    subemotions = subemotion_repository.select_by_emotion(emotion_unsettled)  
    return render_template("students/unsettled.html", students = students, subemotions=subemotions)
  

@students_blueprint.route("/students/out-of-control")
def out_of_control():
    students = student_repository.select_all()
    emotion_out = emotion_repository.select(4)
    subemotions = subemotion_repository.select_by_emotion(emotion_out)  
    return render_template("students/out-of-control.html", students = students, subemotions= subemotions)


 
# CREATE
@students_blueprint.route("/students", methods=['POST'])
def create_feeling():
    student_id = request.form['student_id']
    student= student_repository.select(student_id) 
    subemotion_id= request.form['subemotion_id']
    subemotion= subemotion_repository.select(subemotion_id)
    new_feeling=Feeling(student, subemotion, posting_date=None, id=None)

    feeling_repository.save(new_feeling)
    return redirect("/students")

