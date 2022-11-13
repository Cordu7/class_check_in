import unittest
from models.teacher import Teacher


class TestTeacher(unittest.TestCase):
    
    def setUp(self):
        
        self.teacher = Teacher("Richard", "Smith")

    def test_teacher_has_f_name(self):
        self.assertEqual("Richard", self.teacher.f_name)

    def test_teacher_has_l_name(self):
        self.assertEqual("Smith", self.teacher.l_name)

    def test_teacher_has_id(self):
        self.assertEqual(None, self.teacher.id)

        