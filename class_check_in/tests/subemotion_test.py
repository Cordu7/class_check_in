import unittest
from models.subemotion import Subemotion
from models.emotion import Emotion

class TestEmotion(unittest.TestCase):
    
    def setUp(self):
        self.emotion_1= Emotion("Out of Control")
        self.subemotion= Subemotion("Angry", self.emotion_1)

    def test_subemotion_name(self):
        self.assertEqual("Furious", self.subemotion.subemotion_name)

    def test_subemotion_emotio (self):
        self.assertEqual(self.emotion_1, self.subemotion.emotion)

    def test_emotion_has_id(self):
        self.assertEqual(None, self.emotion_1.id)