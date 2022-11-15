from db.run_sql import run_sql
from models.bagged_munro import Bagged_munro
import pdb

def save(bagged_munro):
    sql = "INSERT INTO munros (name_id, date) VALUES (%s, %s) RETURNING id"
    values = [munro.name.id, bagged_munro.date]
    results = run_sql(sql, values)
    id = results[0]['id']
    munro.id = id

# def select_all():
#     munros = []
#     sql = "SELECT * FROM munros"
#     results = run_sql(sql)
#     for row in results:
#         munro = Munro(result["name"], result["region"], result["altitude"], result["status"], result["date"], result["id"])
#         munros.append(munro)
#     return munros


# def select(id):
#     munro = None 
#     sql = "SELECT * FROM munros WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     if results:
#         result = results[0]
#         munro = Munro(result["name"], result["region"], result["altitude"], result["status"], result["date"], result["id"])
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
