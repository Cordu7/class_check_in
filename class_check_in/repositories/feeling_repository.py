from db.run_sql import run_sql
import datetime
from models.feeling import Feeling
from models.student import Student
from models.subemotion import Subemotion
import repositories.subemotion_repository as subemotion_repository
import repositories.pupil_repository as student_repository
import pdb


# SELECT students.id AS student_id,  subemotions.subemotion_name, feelings.posting_date
# FROM students
# INNER JOIN feelings ON students.id =feelings.student_id
# INNER JOIN subemotions ON subemotions.id = feelings.subemotion_id

# ORDER BY posting_date, student_id


# def select_student_emotion():
#     students = []
#     subemotions = []
#     feelings = []
#     sql = "SELECT  %s, %s , %s FROM students INNER JOIN feelings ON %s = %s INNER JOIN subemotions ON %s = %s"
#     values = [ students.id, subemotions.id,  students.id, feelings.student_id, subemotions.id, feelings.subemotion_id, feelings.student_id ]
#     results = run_sql(sql, values)
#     print(results)

def save(feeling):
    sql = "INSERT INTO feelings (student_id, subemotion_id) VALUES (%s, %s) RETURNING *"
    values = [feeling.student.id, feeling.subemotion.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    feeling.id = id



# def select_all():
#     feelings = []
#     sql = "SELECT * FROM feelings"
#     results = run_sql(sql)
#     for result in results:
#         student = student_repository.select(result["student_id"])
#         subemotion = subemotion_repository.select(result["subemotion_id"])
#         # posting_date = subemotion_repository.select(result["posting_date"])
#         # format = '%Y-%m-%d %H:%M:%S'
#         # python_date= posting_date.strftime(format)  
#         # pdb.set_trace()
#         # feeling = Feeling(student, subemotion, python_date, result["id"])
#         feelings.append(feeling)
       
#     return feelings

def select_by_student(student):
    feelings = []
    sql = "SELECT * FROM feelings WHERE student_id = %s ORDER BY posting_date"
    values =[student.id]
    results = run_sql(sql, values)
    for result in results:
        student = student_repository.select(result["student_id"])
        subemotion = subemotion_repository.select(result["subemotion_id"])
        date=result["posting_date"]
        # format = '%Y-%m-%d %H:%M:%S'
        # python_date= date.strftime(format)  
        feeling = Feeling(student, subemotion, date, result["id"])
        feelings.append(feeling)  
    return feelings



# def select(id):
#     feeling = None 
#     sql = "SELECT * FROM feelings WHERE id = %s"
#     values = [id]

#     results = run_sql(sql, values)


#     if results:
#         result = results[0]
#         student = student_repository.select(result["student_id"])
#         subemotion = subemotion_repository.select(result["subemotion_id"])
#         time = subemotion_repository.select(result["time"])
#         feeling = Feeling(student, subemotion, result["id"])
#     return feeling



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
