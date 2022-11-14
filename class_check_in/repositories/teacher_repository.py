from db.run_sql import run_sql

from models.teacher import Teacher


def save(teacher):
    sql = "INSERT INTO teachers (f_name, l_name) VALUES (%s, %s) RETURNING *"
    values = [teacher.f_name, teacher.l_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    teacher.id = id
    return teacher


def select_all():
    teachers = []

    sql = "SELECT * FROM teachers"
    results = run_sql(sql)

    for row in results:
        teacher = Teacher(row['f_name'], row['l_name'], row['id'] )
        teachers.append(teacher)
    return teachers


def select(id):
    teacher = None
    sql = "SELECT * FROM teachers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        teacher = Teacher(result['f_name'], result['l_name'], result['id'] )
    return teacher


def delete_all():
    sql = "DELETE  FROM teachers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM teachers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(teacher):
    sql = "UPDATE teachers SET (f_name, l_name) = (%s, %s) WHERE id = %s"
    values = [teacher.f_name, teacher.l_name, teacher.id]
    run_sql(sql, values)


