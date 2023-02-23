#Individual Project: class_check_in

## Brief:

### Student's Well_being Tracker App

A primary school wants to build an app for teachers to support their students well-being. One teacher has a many students of students. (One to many mapping)

#### MVP

- The school wants to be able to register students and then keep a reckord of their well-being. 
The well-being is self-assessed since the school wants to teach the students to be reflective and to self-regulate.

- Be able to assign students to teachers

- each students can choose the emotions they are feeling at two points during the day and the app records this

- A teacher can view a students feelings 


## Installation
Python 3 and postgreSQL are required to install the app.

To install the dependencies, build the database structure and launch with starter data, run the following commands in your CLI:

pip3 install -r requirements.txt
createdb class_check_in
psql -d class_check_in -f db/class_check_in.sql
python3 console.py

To run the app:

flask run
