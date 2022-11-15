from db.run_sql import run_sql
from models.munro import Munro
from models.region import Region
import repositories.region_repository as region_repository
import pdb

def save(munro):
    sql = "INSERT INTO munros (name, region_id, altitude) VALUES (%s, %s, %s) RETURNING id"
    values = [munro.name, munro.region.id, munro.altitude]
    results = run_sql(sql, values)
    id = results[0]['id']
    munro.id = id

def select_all():
    munros = []
    sql = "SELECT * FROM munros"
    results = run_sql(sql)
    for result in results:
        region_id = result['region_id'] # result here is pulling by column_name
        region = region_repository.select(region_id)
        munro = Munro(result["name"], region, result["altitude"], result["id"])
        munros.append(munro)
    return munros


# def select(id):
#     munro = None 
#     sql = "SELECT * FROM munros WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     if results:
#         result = results[0]
#         munro = Munro(result["name"], result["region"], result["altitude"], result["date"], result["id"])
#     return munro


def delete_all():
    sql = "DELETE FROM munros"
    run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM munros WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(munro):
#     sql = "UPDATE munros SET name = %s WHERE id = %s"
#     values = [munro.name, munro.id]
#     run_sql(sql, values)
