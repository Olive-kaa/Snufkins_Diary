from db.run_sql import run_sql
from models.region import Region
import pdb

def save(region):
    sql = "INSERT INTO regions (name) VALUES (%s) RETURNING id"
    values = [region.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    region.id = id

def select(id):
    region = None
    sql = "SELECT * FROM regions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        region = Region(result["name"], result["id"])
    return region

def select_all():
    regions = []
    sql = "SELECT * FROM regions"
    results = run_sql(sql)
    for result in results:
        region = Region(result["name"], result["id"])
        regions.append(region)
    return regions

def delete_all():
    sql = "DELETE FROM regions"
    run_sql(sql)
