DROP TABLE IF EXISTS emotions CASCADE;
DROP TABLE IF EXISTS subemotions CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS feelings CASCADE;
DROP TABLE IF EXISTS teachers;




CREATE TABLE teachers(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    name VARCHAR(255)
    );


CREATE TABLE emotions(
    id SERIAL PRIMARY KEY,
    emotion_name VARCHAR(255) 
    );

CREATE TABLE subemotions(
    id SERIAL PRIMARY KEY,
    subemotion_name VARCHAR(255),
    emotion_id INT NOT NULL REFERENCES emotions(id) ON DELETE CASCADE 
    );



CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    teacher_id INT NOT NULL REFERENCES teachers(id) ON DELETE CASCADE
    );

CREATE TABLE feelings (
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES students(id)ON DELETE CASCADE,
    subemotion_id INT NOT NULL REFERENCES subemotions(id) ON DELETE CASCADE,
    posting_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)


