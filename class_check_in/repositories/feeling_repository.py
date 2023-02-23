from db.run_sql import run_sql
from models.feeling import Feeling
from models.student import Student
from models.subemotion import Subemotion
import repositories.subemotion_repository as subemotion_repository
import repositories.pupil_repository as student_repository
import pdb

def save(feeling):
    sql = "INSERT INTO feelings (student_id, subemotion_id) VALUES (%s, %s) RETURNING *"
    values = [feeling.student.id, feeling.subemotion.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    feeling.id = id

def select_by_student(student):
    feelings = []
    sql = "SELECT * FROM feelings WHERE student_id = %s ORDER BY posting_date"
    values =[student.id]
    results = run_sql(sql, values)
    for result in results:
        student = student_repository.select(result["student_id"])
        subemotion = subemotion_repository.select(result["subemotion_id"])
        date=result["posting_date"] 
        feeling = Feeling(student, subemotion, date, result["id"])
        feelings.append(feeling)  
    return feelings


