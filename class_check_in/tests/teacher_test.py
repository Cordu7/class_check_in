import unittest
from models.teacher import Teacher

class TestTeacher(unittest.TestCase):
    
    def setUp(self):
        
        self.teacher = Teacher("Ms", "Richard")

    def test_teacher_has_name(self):
        self.assertEqual("Richard", self.teacher.name)

    def test_teacher_has_title(self):
        self.assertEqual("Ms", self.teacher.title)

    def test_teacher_has_id(self):
        self.assertEqual(None, self.teacher.id)
