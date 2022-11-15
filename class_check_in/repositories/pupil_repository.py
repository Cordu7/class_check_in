from db.run_sql import run_sql

from models.student import Student


def save(student):
    sql = "INSERT INTO students (f_name, l_name, d_o_b, gender, teacher) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [student.f_name, student.l_name, student.d_o_b, student.gender, student.teacher.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    student.id = id
    

def select_all():
    students = []

    sql = "SELECT * FROM students"
    results = run_sql(sql)

    for result in results:
        student = Student(result['f_name'], result['l_name'],result['d_o_b'], result['gender'], result['teacher'], result['id'] )
        students.append(student)
    return students


def select(id):
    student = None
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        student = Student(result['f_name'], result['l_name'],result['d_o_b'], result['gender'],result['teacher'], result['id'] )
    return student


def delete_all():
    sql = "DELETE  FROM students"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM students WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(student):
    sql = "UPDATE students SET (f_name, l_name, d_o_b, gender, teacher) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [student.f_name, student.l_name, student.d_o_b, student.gender, student.teacher.id, student.id]
    run_sql(sql, values)