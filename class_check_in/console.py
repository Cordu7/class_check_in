import pdb
import datetime
from models.carer import Carer
from models.teacher import Teacher
from models.student import Student
from models.emotion import Emotion



import repositories.teacher_repository as teacher_repository
import repositories.emotion_repository as emotion_repository

#carer_1= Carer("John", "Miller", "2 Burton Way, EH1112B, Edinburgh", "1234567")

teacher = Teacher("Richard", "Smith")
teacher_repository.save(teacher)

# student_1 = Student("Harris", "Hall", datetime.date(2004,12,10), "male", teacher, carer_1) 

emotion1= Emotion("Low")
emotion2= Emotion("Ready to learn")
emotion3= Emotion("Unsettled")
emotion4= Emotion("Out of control")

# emotion_repository.save(emotion1)
# emotion_repository.save(emotion2)
# emotion_repository.save(emotion3)
# emotion_repository.save(emotion4)

