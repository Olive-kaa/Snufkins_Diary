from flask import Blueprint, Flask, redirect, render_template, request
from models.bagged_munro import Bagged_munro

# from models.bagged_munro import Bagged_munro
import repositories.bagged_munro_repository as bagged_munro_repository
import repositories.hiker_repository as hiker_repository
import repositories.munro_repository as munro_repository

bagged_munros_blueprint = Blueprint("bagged_munros", __name__)

# INDEX
@bagged_munros_blueprint.route("/munros")
def munros():
    bagged_munros = bagged_munro_repository.select_all()
    return render_template("munros/index.html", munros=munros)

@bagged_munros_blueprint.route("/bagged_munros", methods=["POST"])
def create_bagged_munro():
    hiker_id = request.form["hiker_id"]
    munro_id = request.form["munro_id"]
    date_bagged = request.form["date_bagged"]
    hiker = hiker_repository.select(hiker_id)
    munro = munro_repository.select(munro_id)
    new_bagged_munro = Bagged_munro(hiker, munro, date_bagged)
    bagged_munro_repository.save(new_bagged_munro)
    return redirect("/hikers")