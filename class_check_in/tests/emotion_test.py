import unittest
from models.emotion import Emotion
import datetime


class TestEmotion(unittest.TestCase):
    
    def setUp(self):
        self.emotion_1= Emotion("Out of Control")

    

    def test_emotion_name(self):
        self.assertEqual("Out of Control", self.emotion_1.emotion_name)

    
