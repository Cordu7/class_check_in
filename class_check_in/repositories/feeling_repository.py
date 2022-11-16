from db.run_sql import run_sql
from models.feeling import Feeling
from models.student import Student
from models.subemotion import Subemotion
import repositories.subemotion_repository as subemotion_repository
import repositories.pupil_repository as student_repository




def save(feeling):
    sql = "INSERT INTO feelings (student_id, subemotion_id, time) VALUES (%s, %s, %s) RETURNING *"
    values = [feeling.student_id.id, feeling.subemotion_id.id, feeling.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    feeling.id = id


def select_all():
    feelings = []
    sql = "SELECT * FROM feelings"
    results = run_sql(sql)
    for result in results:
        student = student_repository.select(result["student_id"])
        subemotion = subemotion_repository.select(result["subemotion_id"])
        time = subemotion_repository.select(result["time"])
        feeling = Feeling(student, subemotion, time, result["id"])
        feelings.append(feeling)
    return feelings


def select(id):
    feeling = None 
    sql = "SELECT * FROM feelings WHERE id = %s"
    values = [id]

    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        student = student_repository.select(result["student_id"])
        subemotion = subemotion_repository.select(result["subemotion_id"])
        time = subemotion_repository.select(result["time"])
        feeling = Feeling(student, subemotion, result["id"])
    return feeling


# def delete_all():
#     sql = "DELETE FROM feelings"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM feelings WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(feeling):
#     sql = "UPDATE feelings SET (student_id, subemotion_id) = (%s, %s) WHERE id = %s"
#     values = [feeling.student.id, feeling.subemotion.id, feeling.id]
#     run_sql(sql, values)
