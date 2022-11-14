from db.run_sql import run_sql

from models.carer import Carer


def save(carer):
    sql = "INSERT INTO carers (f_name, l_name, details, phone_num) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [carer.f_name, carer.l_name, carer.details, carer.phone_num ]
    results = run_sql(sql, values)
    id = results[0]['id']
    carer.id = id
    


def select_all():
    carers = []

    sql = "SELECT * FROM carers"
    results = run_sql(sql)

    for result in results:
        carer = Carer(result['f_name'], result['l_name'],result['details'], result['phone_num'],result['id'] )
        carers.append(carer)
    return carers


def select(id):
    carer = None
    sql = "SELECT * FROM carers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        carer = Carer(result['f_name'], result['l_name'],result['details'], result['phone_num'],result['id'] )
    return carer


def delete_all():
    sql = "DELETE  FROM carers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM carers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(carer):
    sql = "UPDATE carers SET (f_name, l_name, details, phone_num) = (%s, %s, %s, %s) WHERE id = %s"
    values = [carer.f_name, carer.l_name,  carer.details, carer.phone_num, carer.id]
    run_sql(sql, values)