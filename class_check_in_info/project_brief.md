### Student's Well_being Tracker App

A primary school wants to build an app for teachers to support their students well-being. One teacher has a many students of students. (One to many mapping)



#### MVP

- The school wants to be able to register students and then keep a reckord of their will-beeing. The well-being is self-assessed since the school wants to teach the students to be reflective and to self-regulate.

 Important information for the school to know is -
  - Name
  - Date Of Birth (use a VARCHAR initially)
  - Gender (male/female/binary)
  - Contact details for the parents

  
- Be able to assign students to teachers

- each students chooses the emotions they are feeling at two points during the day and the app records this

- A teacher can view a single students feelings or the entire classes feelings

- CRUD actions for teachers / students - remember the user - what would they want to see on each View? What Views should there be?

### Possible Extensions

- 

- Mark students as being attending/not attending at school. Not attending students  won't be able to add any emotions and are recorded as absent.

- If a parent has multiple children we don't want to keep updating contact details separately for each child. Extend your application to reflect that a parent can have many children and to more sensibly keep track of parents details (avoiding repetition / inconsistencies)

- Handle  dates/ use date for DOB

Add extra functionality of your choosing:
- assigning actions the student can undertake when a student is feeling a certain way and  students can add an action that gets them ready to learn
- Teacher to be able to add notes to students over time. 
- Add that students can have more than one teacher.
- students can take note of triggers that cause them to feel a certain way
- teacher can add notes to students
