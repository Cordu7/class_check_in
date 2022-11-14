import pdb
import datetime
from models.carer import Carer
from models.teacher import Teacher
from models.student import Student
import repositories.teacher_repository as teacher_repository

#carer_1= Carer("John", "Miller", "2 Burton Way, EH1112B, Edinburgh", "1234567")

teacher = Teacher("Richard", "Smith")
teacher_repository.save(teacher)

# student_1 = Student("Harris", "Hall", datetime.date(2004,12,10), "male", teacher, carer_1) 



