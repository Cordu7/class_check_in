from db.run_sql import run_sql
import pdb

from models.teacher import Teacher


def save(teacher):
    sql = "INSERT INTO teachers (title, name) VALUES (%s, %s) RETURNING *"
    values = [teacher.title, teacher.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    teacher.id = id
    #return teacher


def select_all():
    teachers = []

    sql = "SELECT * FROM teachers"
    results = run_sql(sql)

    for result in results:
        teacher = Teacher(result['title'], result['name'], result['id'] )
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
        teacher = Teacher(result['title'], result['name'], result['id'] )
    return teacher


def delete_all():
    sql = "DELETE  FROM teachers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM teachers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(teacher):
    sql = "UPDATE teachers SET (title, name) = (%s, %s) WHERE id = %s"
    values = [teacher.title, teacher.name, teacher.id]
    run_sql(sql, values)


