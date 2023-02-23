import unittest
from models.student import Student
from models.teacher import Teacher



class TestStudent(unittest.TestCase):
    
    def setUp(self):

        
        self.teacher = Teacher("Mx", "Smith")
        self.student_1 = Student("Harris", self.teacher) 
      

    def test_student_has_name(self):
        self.assertEqual("Harris", self.student_1.name)



    def test_student_has_teacher(self):
        self.assertEqual(self.teacher, self.student_1.teacher)

    def test_student_has_id(self):
        self.assertEqual(None, self.student_1.id)

    


