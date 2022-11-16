from db.run_sql import run_sql
from models.bagged_munro import Bagged_munro
from models.munro import Munro
from models.hiker import Hiker
from repositories import hiker_repository
from repositories import munro_repository
import pdb

def save(bagged_munro):
    sql = "INSERT INTO bagged_munros (hiker_id, munro_id, date_bagged) VALUES (%s, %s, %s) RETURNING id"
    values = [bagged_munro.hiker.id, bagged_munro.munro.id, bagged_munro.date_bagged]
    results = run_sql(sql, values)
    id = results[0]['id']
    bagged_munro.id = id

def select_all():
    bagged_munros = []
    sql = "SELECT * FROM bagged_munros"
    results = run_sql(sql)
    for result in results:
        hiker_id = result['hiker_id']
        hiker = hiker_repository.select(hiker_id)
        munro_id = result['munro_id']
        munro = munro_repository.select(munro_id)
        bagged_munro = Bagged_munro(hiker, munro, result["id"])
        bagged_munros.append(bagged_munro)
    return bagged_munros


def select(id):
    bagged_munro = None 
    sql = "SELECT * FROM bagged_munros WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        bagged_munro = Bagged_munro(result["hiker_id"], result["munro_id"], result["date"], result["id"])
    return bagged_munro


def delete_all():
    sql = "DELETE FROM bagged_munros"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bagged_munros WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(bagged_munro):
    sql = "UPDATE bagged_munros SET (hiker_id, munro_id, date) = (%s, %s, %s) WHERE id = %s"
    values = [bagged_munro.hiker_id, bagged_munro.munro_id, bagged_munro_date]
    run_sql(sql, values)
