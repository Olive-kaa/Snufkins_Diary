from flask import Blueprint, Flask, redirect, render_template, request
import pdb
from models.munro import Munro
from models.region import Region
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository

munros_blueprint = Blueprint("munros", __name__)

# INDEX
@munros_blueprint.route("/munros")
def munros():
    munros = munro_repository.select_all()
    return render_template("munros/index.html", munros=munros)

# NEW
@munros_blueprint.route("/munros/new")
def new_munro():
    regions = region_repository.select_all()
    return render_template("munros/new.html", regions=regions)


# CREATE
@munros_blueprint.route("/munros", methods=["POST"])
def create_munro():
    input_name = request.form["name"]
    region_id = request.form["region_id"]
    selected_region = region_repository.select(region_id)
    input_altitude = request.form["altitude"]
    new_munro = Munro(input_name, selected_region, input_altitude)
    munro_repository.save(new_munro)
    return redirect("/munros")


# EDIT
@munros_blueprint.route("/munros/<id>/edit")
def edit_munro(id):
    munro = munro_repository.select(id)
    # regions = region_repository.select_all()
    return render_template('munros/edit.html', munro=munro)


# UPDATE
@munros_blueprint.route("/munros/<id>", methods=["POST"])
def update_munro(id):
    munro_name = request.form["name"]
    region_id = request.form["region_id"]
    selected_region = region_repository.select(region_id)
    altitude = request.form["altitude"]
    munro = Munro(name, region, altitude, id)
    munro_repository.update(munro)
    return redirect('/munros')


# DELETE
@munros_blueprint.route("/munros/<id>/delete", methods=["POST"])
def delete_munro(id):
    munro_repository.delete(id)
    return redirect('/munros')
