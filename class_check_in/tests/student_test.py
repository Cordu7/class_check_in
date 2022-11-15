import unittest
from models.student import Student
from models.teacher import Teacher
from models.carer import Carer
import datetime


class TestStudent(unittest.TestCase):
    
    def setUp(self):

        self.carer_1= Carer("John", "Miller", "2 Burton Way, EH1112B, Edinburgh", "1234567")
        self.teacher = Teacher("Richard", "Smith")
        self.student_1 = Student("Harris", "Hall", datetime.date(2004,12,10), "male", self.teacher) 
      

    def test_student_has_f_name(self):
        self.assertEqual("Harris", self.student_1.f_name)

    def test_student_has_l_name(self):
        self.assertEqual("Hall", self.student_1.l_name)

    def test_student_has_dob(self):
        self.assertEqual(("2004-12-10"), str(self.student_1.d_0_b))

    def test_student_has_gender(self):
        self.assertEqual("male", self.student_1.gender)

    def test_student_has_teacher(self):
        self.assertEqual(self.teacher, self.student_1.teacher)

    def test_student_has_id(self):
        self.assertEqual(None, self.student_1.id)

    


