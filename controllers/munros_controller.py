from flask import Blueprint, Flask, redirect, render_template, request

from models.munro import Munro
import repositories.munro_repository as munro_repository

munros_blueprint = Blueprint("munros", __name__)

# INDEX
@munros_blueprint.route("/munros")
def munros():
    munros = munro_repository.select_all()
    return render_template("munros/index.html", munros=munros)

