-- Create a database
CREATE DATABASE student_db;

-- Use the database
USE student_db;

-- Create a table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

-- Insert sample data
INSERT INTO students (name, age) VALUES ('Alice', 22), ('Bob', 24);
