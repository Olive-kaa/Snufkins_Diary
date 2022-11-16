from flask import Blueprint, Flask, redirect, render_template, request
import pdb
from models.hiker import Hiker
from models.munro import Munro
from models.region import Region
from models.bagged_munro import Bagged_munro
import repositories.hiker_repository as hiker_repository
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository
import repositories.bagged_munro_repository as bagged_munro_repository

hikers_blueprint = Blueprint("hikers", __name__)

# INDEX
@hikers_blueprint.route("/hikers")
def hikers():
    hikers = hiker_repository.select_all()
    return render_template("hikers/index.html", hikers=hikers)

# SHOW
@hikers_blueprint.route("/hikers/<id>")
def hiker(id):
    single_hiker = hiker_repository.select(id)
    munros = munro_repository.select_all()
    regions = region_repository.select_all()
    climbs = hiker_repository.bagged_munros(id)
    climb1 = climbs[0]

    return render_template("hikers/show.html", hiker=single_hiker, climbs=climbs, munros=munros)


# NEW
@hikers_blueprint.route("/hikers/new")
def new_hiker():
    return render_template("hikers/new.html")


# CREATE
@hikers_blueprint.route("/hikers", methods=["POST"])
def create_hiker():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_hiker = Hiker(first_name, last_name)
    hiker_repository.save(new_hiker)
    return redirect("/hikers")


# EDIT
@hikers_blueprint.route("/hikers/<id>/edit")
def edit_hiker(id):
    hiker = hiker_repository.select(id)
    return render_template('hikers/edit.html', hiker=hiker)


# UPDATE
@hikers_blueprint.route("/hikers/<id>", methods=["POST"])
def update_hiker(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    hiker = Hiker(first_name, last_name, id)
    hiker_repository.update(hiker)
    return redirect('/hikers')


# DELETE
@hikers_blueprint.route("/hikers/<id>/delete", methods=["POST"])
def delete_hiker(id):
    hiker_repository.delete(id)
    return redirect('/hikers')
