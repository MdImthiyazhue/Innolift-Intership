-- Day 44 — Database setup for Student Management
-- Run with: mysql -u root -p < database/schema.sql

CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL
);

-- Sample records (at least 5, as required by Task 01)
INSERT INTO students (name, email, course) VALUES
    ('Arun Kumar', 'arun.kumar@example.com', 'AI & Data Science'),
    ('Divya Sri', 'divya.sri@example.com', 'AI & Data Science'),
    ('Mohamed Imthiyaz', 'imthiyaz@example.com', 'AI & Data Science'),
    ('Sneha Reddy', 'sneha.reddy@example.com', 'Computer Science'),
    ('Karthik Raja', 'karthik.raja@example.com', 'Information Technology')
ON DUPLICATE KEY UPDATE name = VALUES(name);

-- Verify:
-- SELECT * FROM students;
