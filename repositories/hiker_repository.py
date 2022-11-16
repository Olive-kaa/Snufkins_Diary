from db.run_sql import run_sql
from models.hiker import Hiker
from models.bagged_munro import Bagged_munro
import repositories.munro_repository as munro_repository
import pdb

def save(hiker):
    sql = "INSERT INTO hikers (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [hiker.first_name, hiker.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    hiker.id = id

def select_all():
    hikers = []
    sql = "SELECT * FROM hikers"
    results = run_sql(sql)
    for result in results:
        hiker = Hiker(result["first_name"], result["last_name"], result["id"])
        hikers.append(hiker)
    return hikers

def select(id):
    hiker = None 
    sql = "SELECT * FROM hikers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        hiker = Hiker(result["first_name"], result["last_name"], result["id"])
    return hiker

def update(hiker):
    sql = "UPDATE hikers SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [hiker.first_name, hiker.last_name, hiker.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM hikers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM hikers"
    run_sql(sql)

def bagged_munros(hiker_id):
    climbs = []
    sql = """SELECT munro_id, date_bagged FROM bagged_munros 
    WHERE hiker_id = %s  GROUP BY hiker_id, munro_id, date_bagged"""
    values = [hiker_id]
    results = run_sql(sql, values)
    hiker = select(hiker_id)
    for result in results:
        munro = munro_repository.select(result["munro_id"])
        date_bagged = result["date_bagged"]
        current_climb = Bagged_munro(hiker, munro, date_bagged)
        climbs.append(current_climb)
        # Rebuilding our bagged munro class from different sections of the database using the ids of the bagged hikes table
    return climbs