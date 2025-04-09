-- Basic schema for student table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    attendance FLOAT,
    maths INT,
    science INT,
    english INT
);
