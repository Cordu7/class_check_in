import unittest
from models.emotion import Emotion
import datetime


class TestEmotion(unittest.TestCase):
    
    def setUp(self):
        self.emotion_1= Emotion("Out of Control")

    def test_emotion_name(self):
        self.assertEqual("Out of Control", self.emotion_1.emotion_name)

    def test_emotion_has_id(self):
        self.assertEqual(None, self.emotion_1.id)

    def test_emotion_has_empty_list(self):
        self.assertEqual([], self.emotion_1.emotion_list)

    # def test_emotion_has_time(self):
    #     self.assertEqual(datetime.datetime.now(), self.emotion_1.date)

