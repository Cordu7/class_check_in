import unittest;
from models.feeling import Feeling
from models.student import Student
from models.teacher import Teacher
from models.subemotion import Subemotion
from models.emotion import Emotion


class TestFeeling(unittest.TestCase):
    
    def setUp(self):
        self.emotion_1= Emotion("Out of Control")
        self.subemotion= Subemotion("Angry", self.emotion_1)
        self.teacher = Teacher("Mx", "Smith")
        self.student_1 = Student("Harris", self.teacher) 
        self.feeling = Feeling(self.student_1, self.emotion_1)
        

    def test_feeling_has_student(self):
        self.assertEqual(self.student_1, self.feeling.student)

    def test_emotion_has_time(self):
        self.assertEqual(None, self.feeling.id)

    def test_emotion_has_posting_date(self):
        self.assertEqual(None, self.feeling.posting_date)