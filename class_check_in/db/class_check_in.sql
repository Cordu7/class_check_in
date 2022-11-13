DROP TABLE IF EXISTS carers;
DROP TABLE IF EXISTS emotions;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;

CREATE TABLE carers (
  id SERIAL PRIMARY KEY,
  f_name VARCHAR(255),
  l_name VARCHAR(255),
  details VARCHAR(255),
  phone_num VARCHAR(25),
);

CREATE TABLE teachers (
  id SERIAL PRIMARY KEY,
  f_name VARCHAR(255),
  l_name VARCHAR(255),
);


CREATE TABLE emotions (
  id SERIAL PRIMARY KEY,
  emotion_name VARCHAR(255),
  emotion_list VARCHAR(255),
  emotion_date VARCHAR(255)

);
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  f_name VARCHAR(255),
  l_name VARCHAR(255),
  d_o_b VARCHAR(255)
  gender VARCHAR(255)
  teacher INT NOT NULL REFERENCES teachers(id)
  carer INT NOT NULL REFERENCES carers(id)

);

