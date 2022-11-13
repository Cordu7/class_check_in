import datetime

class Emotion:
    def __init__(self, emotion_name, id= None):
        self.emotion_name= emotion_name
        self.emotion_list= []
        self.id = id
        self.date= datetime.datetime.now()

    def add_emotion(self, emotion):
        self.emotion_list.append(emotion)