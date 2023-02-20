from db.run_sql import run_sql
import pdb

from models.student import Student
from models.teacher import Teacher


def save(student):
    sql = "INSERT INTO students (name, teacher_id) VALUES (%s, %s) RETURNING *"
    values = [student.name, student.teacher.id]
    results = run_sql(sql, values)
    # pdb.set_trace()
    id = results[0]['id']
    student.id = id
    

def select_all():
    students = []

    sql = "SELECT * FROM students"
    results = run_sql(sql)

    for result in results:
        student = Student(result['name'], result['teacher_id'], result['id'] )
        students.append(student)
    return students


def select(id):
    student = None
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        student = Student(result['name'],result['teacher_id'], result['id'] )
    return student


def delete_all():
    sql = "DELETE  FROM students"
    run_sql(sql)



def delete(id):
    sql = "DELETE  FROM students WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(student):
    sql = "UPDATE students SET (name, teacher_id) = (%s, %s) WHERE id = %s"
    values = [student.name, student.teacher.id, student.id]
    run_sql(sql, values)