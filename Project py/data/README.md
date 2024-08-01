# Database Schema

This document provides the schema for the database used in the college registration system. The database consists of three main tables: `departments`, `students`, and `registrations`.

## Departments Table

| Column Name       | Data Type | Constraints               | Description                           |
| ----------------- | --------- | ------------------------- | ------------------------------------- |
| `department_id`   | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique identifier for the department. |
| `department_name` | TEXT      | NOT NULL                  | Name of the department.               |
| `description`     | TEXT      |                           | Description of the department.        |

## Students Table

| Column Name     | Data Type | Constraints                                                 | Description                                    |
| --------------- | --------- | ----------------------------------------------------------- | ---------------------------------------------- |
| `student_id`    | INTEGER   | PRIMARY KEY AUTOINCREMENT                                   | Unique identifier for the student.             |
| `name`          | TEXT      | NOT NULL                                                    | Name of the student.                           |
| `national_id`   | TEXT      | UNIQUE NOT NULL                                             | Unique national ID of the student.             |
| `department_id` | INTEGER   | NOT NULL, FOREIGN KEY REFERENCES departments(department_id) | Department to which the student belongs.       |
| `level`         | INTEGER   | NOT NULL                                                    | Level or year of the student.                  |
| `hours_passed`  | INTEGER   | NOT NULL                                                    | Number of credit hours the student has passed. |
| `gpa`           | REAL      | NOT NULL                                                    | Grade Point Average of the student.            |

## Registrations Table

| Column Name                          | Data Type | Constraints                                                 | Description                                                                    |
| ------------------------------------ | --------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `registration_id`                    | INTEGER   | PRIMARY KEY AUTOINCREMENT                                   | Unique identifier for the registration.                                        |
| `student_id`                         | INTEGER   | NOT NULL, FOREIGN KEY REFERENCES students(student_id)       | Student involved in the registration.                                          |
| `department_id`                      | INTEGER   | NOT NULL, FOREIGN KEY REFERENCES departments(department_id) | Department for which the student is registered.                                |
| `UNIQUE (student_id, department_id)` |           | UNIQUE                                                      | Ensures that a student cannot register for the same department more than once. |
