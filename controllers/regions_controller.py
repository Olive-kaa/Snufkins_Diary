from flask import Blueprint, Flask, redirect, render_template, request

from models.region import Region
import repositories.region_repository as region_repository

regions_blueprint = Blueprint("regions", __name__)

# INDEX
@regions_blueprint.route("/regions")
def regions():
    regions = region_repository.select_all()
    return render_template("regions/index.html", regions=regions)

# NEW
@regions_blueprint.route("/regions/new")
def new_region():
    return render_template("regions/new.html")


# CREATE
@regions_blueprint.route("/regions", methods=["POST"])
def create_region():
    input_name = request.form["name"]
    new_region = Region(input_name)
    region_repository.save(new_region)
    return redirect("/regions")