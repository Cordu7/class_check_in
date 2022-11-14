from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.carer import Carer
import repositories.carer_repository as carer_repository


carers_blueprint = Blueprint("carers", __name__)

@carers_blueprint.route("/carers")
def carers():
    carers = carer_repository.select_all() # NEW
    return render_template("teachers/carers/index.html", carers = carers)


@carers_blueprint.route("/carers/new")
def new_carer():
    return render_template("teachers/carers/new.html")

# CREATE
@carers_blueprint.route("/carers",  methods=['POST'])
def create_carer():
    f_name    = request.form['f_name']
    l_name = request.form['l_name']    
    details = request.form['details']    
    phone_num= request.form['phone_num']    
    new_carer = Carer(f_name, l_name, details, phone_num)
    carer_repository.save(new_carer)
    return redirect("/carers")


# SHOW
# GET '/books/<id>'
@carers_blueprint.route("/carers/<id>")
def show_carer(id):
    carer = carer_repository.select(id)
    return render_template('teachers/carers/show.html', carer = carer)



# EDIT
# GET '/books/<id>/edit'
@carers_blueprint.route("/carers/<id>/edit")
def edit_carer(id):
    carer = carer_repository.select(id)
    return render_template('teachers/carers/edit.html', carer = carer)

# UPDATE
# PUT '/books/<id>'
@carers_blueprint.route("/carers/<id>", methods=['POST'])
def update_carer(id):
    f_name  = request.form['f_name']
    l_name = request.form['l_name']
    details = request.form['details']    
    phone_num= request.form['phone_num']    
    carer = Carer(f_name, l_name, details, phone_num, id)
    carer_repository.update(carer)
    return redirect('/carers')


# DELETE '/books/<id>'
@carers_blueprint.route("/carers/<id>/delete", methods=['POST'])
def delete_carer(id):
    carer_repository.delete(id)
    return redirect('/carers')
