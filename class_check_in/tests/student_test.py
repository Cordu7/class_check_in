import unittest
from models.student import Student
from models.teacher import Teacher
import datetime


class TestStudent(unittest.TestCase):
    
    def setUp(self):

        self.teacher = Teacher("Richard", "Smith")
        self.student_1 = Student("Harris", "Hall", datetime.date(2004,12,10), "male", self.teacher, '1234567') 

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

    def test_student_has_parent_phone_num(self):
        self.assertEqual("1234567", self.student_1.parent_phone_num)

    def test_student_has_id(self):
        self.assertEqual(None, self.student_1.id)

    


