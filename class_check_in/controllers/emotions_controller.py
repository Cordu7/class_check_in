from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.carer_student import CarerStudent
import repositories.carer_student_repository as carer_student_repository

carersstudents_blueprint = Blueprint("carersstudents_blueprint", __name__)

# INDEX
@carersstudents_blueprint.route("/carersstudents")
def bitings():
    carer_student = carer_student_repository.select_all()
    return render_template("teachers/carers_students/index.html", bitings=bitings)


# NEW
@carersstudents_blueprint.route("/carersstudents/new")
def new_biting():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans=humans, zombies=zombies)


# CREATE
@carersstudents_blueprint.route("/carersstudents", methods=["POST"])
def create_biting():
    human_id = request.form["human_id"]
    zombie_id = request.form["zombie_id"]
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)
    new_biting = Biting(human, zombie)
    biting_repository.save(new_biting)
    return redirect("/carersstudents")


# EDIT
@carersstudents_blueprint.route("/carersstudents/<id>/edit")
def edit_biting(id):
    biting = biting_repository.select(id)
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template('bitings/edit.html', biting=biting, humans=humans, zombies=zombies)


# UPDATE
@carersstudents_blueprint.route("/carersstudents/<id>", methods=["POST"])
def update_biting(id):
    human_id = request.form["human_id"]
    zombie_id = request.form["zombie_id"]
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)
    biting = Biting(human, zombie, id)
    biting_repository.update(biting)
    return redirect("/carersstudents")


# DELETE
@carersstudents_blueprint.route("/carersstudents/<id>/delete", methods=["POST"])
def delete_biting(id):
    biting_repository.delete(id)
    return redirect("/carersstudents")
