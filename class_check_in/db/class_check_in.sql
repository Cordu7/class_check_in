DROP TABLE IF EXISTS carers_students;
DROP TABLE IF EXISTS emotions CASCADE;
DROP TABLE IF EXISTS carers CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS teachers;


CREATE TABLE carers(
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    details VARCHAR(255),
    phone_num VARCHAR(25)
    );

CREATE TABLE teachers(
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255)
    );


CREATE TABLE emotions(
    id SERIAL PRIMARY KEY,
    emotion_category VARCHAR(255) 
    );

CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    d_o_b VARCHAR(255),
    gender VARCHAR(255),
    teacher INT NOT NULL REFERENCES teachers(id) ON DELETE CASCADE
    );

CREATE TABLE carers_students (
    id SERIAL PRIMARY KEY,
    carer_id INT NOT NULL REFERENCES carers(id)ON DELETE CASCADE,
    student_id INT NOT NULL REFERENCES students(id) ON DELETE CASCADE

)


