import pdb
import datetime

# from models.teacher import Teacher
# from models.student import Student
from models.emotion import Emotion
from models.subemotion import Subemotion



import repositories.teacher_repository as teacher_repository
import repositories.emotion_repository as emotion_repository
import repositories.subemotion_repository as subemotion_repository
# import repositories.feeling_repository as feeling_repository

# feeling_repository.select_student_emotion()

# #carer_1= Carer("John", "Miller", "2 Burton Way, EH1112B, Edinburgh", "1234567")

# teacher = Teacher("Richard", "Smith")
# teacher_repository.save(teacher)

# # student_1 = Student("Harris", "Hall", datetime.date(2004,12,10), "male", teacher, carer_1) 
emotion_1= Emotion("Low", 1)
emotion_2= Emotion("Ready to learn", 2)
emotion_3= Emotion("Unsettled", 3)
emotion_4= Emotion("Out of control", 4)

emotion_repository.save(emotion_1)
emotion_repository.save(emotion_2)
emotion_repository.save(emotion_3)
emotion_repository.save(emotion_4)

emotion1= Emotion("Low", 1)
emotion2= Emotion("Ready to learn", 2)
emotion3= Emotion("Unsettled", 3)
emotion4= Emotion("Out of control", 4)



subemotion_tired = Subemotion("Tired", emotion1)
subemotion_sad = Subemotion("Sad", emotion1)
subemotion_worried= Subemotion("Worried", emotion1)
subemotion_hungry_thirsty= Subemotion("Hungry or Thirsty", emotion1)
subemotion_bored= Subemotion("Bored", emotion1)
subemotion_lonely= Subemotion("Lonely", emotion1)

subemotion_repository.save(subemotion_tired)
subemotion_repository.save(subemotion_sad)
subemotion_repository.save(subemotion_worried)
subemotion_repository.save(subemotion_hungry_thirsty)
subemotion_repository.save(subemotion_bored)
subemotion_repository.save(subemotion_lonely)


subemotion_motivated = Subemotion("Motivated", emotion2)
subemotion_energetic= Subemotion("Energetic", emotion2)
subemotion_ready_to_work= Subemotion("Ready to work", emotion2)
subemotion_interested = Subemotion("Interested", emotion2)
subemotion_active= Subemotion("Active", emotion2)
subemotion_creative = Subemotion("Creative", emotion2)

subemotion_repository.save(subemotion_motivated)
subemotion_repository.save(subemotion_energetic)
subemotion_repository.save(subemotion_ready_to_work)
subemotion_repository.save(subemotion_interested)
subemotion_repository.save(subemotion_active)
subemotion_repository.save(subemotion_creative)


subemotion_excited= Subemotion("Excited", emotion3)
subemotion_cross = Subemotion("Cross", emotion3)
subemotion_upset = Subemotion("Upset", emotion3)
subemotion_restless = Subemotion("Restless", emotion3)
subemotion_distracted = Subemotion("Distracted", emotion3)
subemotion_nervous = Subemotion("Nervous", emotion3)

subemotion_repository.save(subemotion_excited)
subemotion_repository.save(subemotion_cross)
subemotion_repository.save(subemotion_upset)
subemotion_repository.save(subemotion_restless)
subemotion_repository.save(subemotion_distracted)
subemotion_repository.save(subemotion_nervous)


subemotion_furious = Subemotion("Furious", emotion4)
subemotion_angry= Subemotion("Angry", emotion4)
subemotion_distraught = Subemotion("Distraught", emotion4)
subemotion_overexcited = Subemotion("Overexcited", emotion4)
subemotion_ecstatic = Subemotion("Ecstatic", emotion4)
subemotion_tormented = Subemotion("Tormented", emotion4)

subemotion_repository.save(subemotion_furious)
subemotion_repository.save(subemotion_distraught)
subemotion_repository.save(subemotion_angry)
subemotion_repository.save(subemotion_overexcited)
subemotion_repository.save(subemotion_ecstatic)
subemotion_repository.save(subemotion_tormented)







