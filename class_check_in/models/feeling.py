import datetime

class Feeling:
       def __init__(self, student, subemotion, posting_date=None,  id= None):
        self.student = student
        self.subemotion = subemotion
        self.posting_date = posting_date
        self.id=id
