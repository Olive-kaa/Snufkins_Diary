from flask import Blueprint, Flask, redirect, render_template, request

# from models.bagged_munro import Bagged_munro
import repositories.bagged_munro_repository as bagged_munro_repository

bagged_munros_blueprint = Blueprint("bagged_munros", __name__)

# INDEX
@bagged_munros_blueprint.route("/munros")
def munros():
    bagged_munros = bagged_munro_repository.select_all()
    return render_template("munros/index.html", munros=munros)

