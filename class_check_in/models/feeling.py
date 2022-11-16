import datetime

class Feeling:
       def __init__(self, student_id, subemotion_id, id= None):
        self.student_id = student_id
        self.subemotion_id = subemotion_id
        self.time= datetime.datetime.now()
        self.id=id
